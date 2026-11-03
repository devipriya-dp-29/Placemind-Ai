from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company, PlacementDrive, Application, MockTest, MockTestResult
from .serializers import (
    CompanySerializer, PlacementDriveSerializer, ApplicationSerializer, 
    MockTestSerializer, MockTestResultSerializer
)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        print(f"DEBUG: CompanyViewSet.list called by user: {request.user}")
        print(f"DEBUG: Queryset count: {self.get_queryset().count()}")
        return super().list(request, *args, **kwargs)

class PlacementDriveViewSet(viewsets.ModelViewSet):
    queryset = PlacementDrive.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = PlacementDriveSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        drive = serializer.save()
        # Notify only eligible students
        from users.models import CustomUser, Notification
        students = CustomUser.objects.filter(role='student')
        
        notifications = []
        for student in students:
            if not hasattr(student, 'student_profile'): continue
            profile = student.student_profile
            
            # Application checks
            if profile.cgpa < drive.min_cgpa: continue
            if profile.arrears_count > drive.max_arrears: continue
            
            if drive.allowed_branches:
                allowed = [b.strip().lower() for b in drive.allowed_branches.split(',')]
                user_branch = profile.department.strip().lower() if profile.department else ""
                if 'all' not in allowed and user_branch not in allowed: continue
                
            notifications.append(Notification(
                recipient=student,
                title=f"New Drive: {drive.company.name}",
                message=f"Hiring for {drive.job_role}. You are eligible! Apply before {drive.deadline.strftime('%d-%m-%Y')}."
            ))
        Notification.objects.bulk_create(notifications)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def send_reminders(self, request, pk=None):
        try:
            drive = self.get_object()
        except PlacementDrive.DoesNotExist:
            return Response({'error': 'Drive not found'}, status=status.HTTP_404_NOT_FOUND)
            
        from users.models import CustomUser, Notification
        from .models import Application
        students = CustomUser.objects.filter(role='student')
        
        notifications = []
        for student in students:
            if not hasattr(student, 'student_profile'): continue
            profile = student.student_profile
            
            if profile.cgpa < drive.min_cgpa: continue
            if profile.arrears_count > drive.max_arrears: continue
            
            if drive.allowed_branches:
                allowed = [b.strip().lower() for b in drive.allowed_branches.split(',')]
                user_branch = profile.department.strip().lower() if profile.department else ""
                if 'all' not in allowed and user_branch not in allowed: continue
                
            # If eligible but hasn't applied
            if not Application.objects.filter(student=student, drive=drive).exists():
                notifications.append(Notification(
                    recipient=student,
                    title=f"Reminder: {drive.company.name} Deadline Approaching",
                    message=f"Don't forget to apply for {drive.job_role} before {drive.deadline.strftime('%d-%m-%Y')}."
                ))
                
        Notification.objects.bulk_create(notifications)
        return Response({'message': f'Reminders sent to {len(notifications)} eligible students.'})

    def perform_update(self, serializer):
        old_instance = self.get_object()
        drive = serializer.save()
        
        from users.models import Notification
        
        # Check if interview date changed
        if old_instance.interview_date != drive.interview_date:
            # Notify all applicants
            applicants = drive.applications.all()
            notifications = []
            for app in applicants:
                notifications.append(Notification(
                    recipient=app.student,
                    title=f"Update: {drive.company.name} Interview",
                    message=f"The interview date for {drive.job_role} has been updated to {drive.interview_date.strftime('%d-%m-%Y %H:%M')}."
                ))
            Notification.objects.bulk_create(notifications)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def apply(self, request, pk=None):
        try:
            drive = self.get_object()
        except PlacementDrive.DoesNotExist:
             return Response({'error': 'Drive not found'}, status=status.HTTP_404_NOT_FOUND)

        user = request.user
        
        # Ensure user is a student
        if not hasattr(user, 'student_profile'):
             return Response({'error': 'Profile not found. Please complete your profile.'}, status=status.HTTP_400_BAD_REQUEST)

        profile = user.student_profile
        
        if profile.account_frozen:
            return Response({'error': 'Your account is frozen due to disciplinary reasons. Contact admin.'}, status=status.HTTP_403_FORBIDDEN)
        
        # --- ELIGIBILITY CHECKS ---

        # 1. CGPA Check
        if profile.cgpa < drive.min_cgpa:
            return Response(
                {'error': f'Not eligible. Min CGPA: {drive.min_cgpa}, Yours: {profile.cgpa}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # 2. Arrears Check
        if profile.arrears_count > drive.max_arrears:
            return Response(
                {'error': f'Not eligible. Max Arrears: {drive.max_arrears}, Yours: {profile.arrears_count}'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # 3. Branch Check
        if drive.allowed_branches:
            allowed = [b.strip().lower() for b in drive.allowed_branches.split(',')]
            user_branch = profile.department.strip().lower() if profile.department else ""
            if 'all' not in allowed and user_branch not in allowed:
                    return Response(
                    {'error': f'Not eligible. Allowed branches: {drive.allowed_branches}. Yours: {user_branch}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # 4. Check if already applied
        if Application.objects.filter(student=user, drive=drive).exists():
            return Response({'message': 'Already applied'}, status=status.HTTP_200_OK)
        
        # --- CREATE APPLICATION ---
        
        # Auto-attach resume from profile if available
        resume = profile.resume if profile.resume else None
        
        Application.objects.create(student=user, drive=drive, resume=resume)
        
        # Notify student of successful application
        from users.models import Notification
        Notification.objects.create(
            recipient=user,
            title=f"Applied: {drive.company.name}",
            message=f"Successfully applied for {drive.job_role}. You will be notified of further updates."
        )
        
        return Response({'message': 'Applied successfully'}, status=status.HTTP_201_CREATED)

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Application.objects.all()
        return Application.objects.filter(student=user)

    def perform_update(self, serializer):
        old_instance = self.get_object()
        application = serializer.save()
        
        if old_instance.status != application.status:
            from users.models import Notification
            
            title = f"Status Update: {application.drive.company.name}"
            message = ""
            
            if application.status == 'shortlisted':
                message = f"Congratulations! You have been shortlisted for {application.drive.job_role}. Check specific interview details."
            elif application.status == 'rejected':
                message = f"Update on your application for {application.drive.job_role}. status: Rejected."
            elif application.status == 'selected':
                message = f"Congratulations! You have been Selected for the role of {application.drive.job_role}!"
            else:
                 message = f"Your application status for {application.drive.job_role} has changed to {application.status}."

            Notification.objects.create(
                recipient=application.student,
                title=title,
                message=message
            )

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def mark_attendance(self, request, pk=None):
        try:
            application = self.get_object()
        except Application.DoesNotExist:
            return Response({'error': 'Application not found'}, status=status.HTTP_404_NOT_FOUND)
            
        status_update = request.data.get('status') # 'present' or 'absent'
        
        if status_update == 'absent':
            profile = application.student.student_profile
            profile.missed_interviews_count += 1
            
            # Logic: 1st miss -> warning, 2nd miss -> freeze
            from users.models import Notification
            
            if profile.missed_interviews_count == 1:
                profile.warning_issued = True
                Notification.objects.create(
                    recipient=application.student,
                    title="Warning: Missed Interview",
                    message=f"You missed the interview for {application.drive.company.name}. Next absence will freeze your account."
                )
            elif profile.missed_interviews_count >= 2:
                profile.account_frozen = True
                Notification.objects.create(
                    recipient=application.student,
                    title="Account Frozen",
                    message=f"You missed the interview for {application.drive.company.name}. Your account is currently frozen due to repeated absence. Contact admin."
                )
            
            profile.save()
            return Response({'message': 'Marked absent. Disciplinary action taken if applicable.'})
            
        return Response({'message': 'Attendance marked.'})

class MockTestViewSet(viewsets.ModelViewSet):
    queryset = MockTest.objects.all()
    serializer_class = MockTestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def personalize(self, request, pk=None):
        test = self.get_object()
        user = request.user
        
        if not hasattr(user, 'student_profile'):
            return Response(self.get_serializer(test).data)
            
        student_skills = [s.strip().lower() for s in user.student_profile.skills.split(',')]
        all_questions = test.questions
        
        # Filter questions where at least one skill tagged matches student skills
        skill_based_questions = []
        for q in all_questions:
            q_skills = [s.lower() for s in q.get('skills', [])]
            # If question has no skill tags, include it anyway as general
            if not q_skills or any(skill in student_skills for skill in q_skills):
                skill_based_questions.append(q)
        
        # If no matches found, fallback to original
        if not skill_based_questions:
            return Response(self.get_serializer(test).data)
            
        data = self.get_serializer(test).data
        data['questions'] = skill_based_questions
        data['title'] = f"{test.title} (Personalized for your Resume)"
        return Response(data)

class MockTestResultViewSet(viewsets.ModelViewSet):
    serializer_class = MockTestResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return MockTestResult.objects.all()
        return MockTestResult.objects.filter(student=user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
