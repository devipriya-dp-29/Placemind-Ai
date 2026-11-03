from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.db import models # Import models to use Q objects properly via models.Q or directly import Q
from placements.models import PlacementDrive, Application, MockTestResult
from users.models import CustomUser, StudentProfile
from django.db.models import Avg, Count, Q

class PredictRiskView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        if not hasattr(user, 'student_profile'):
             return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        
        profile = user.student_profile
        
        # Simple Rule-based Risk Prediction
        # Factors: CGPA, Arrears, Mock Test Scores, Attendance
        
        risk_score = 0
        reasons = []
        
        # 1. CGPA Analysis
        if profile.cgpa < 6.0:
            risk_score += 3
            reasons.append("Low CGPA")
        elif profile.cgpa < 7.5:
            risk_score += 1
            
        # 2. Arrears
        if profile.arrears_count > 0:
            risk_score += 2 * profile.arrears_count
            reasons.append(f"{profile.arrears_count} Arrears")
            
        # 3. Attendance
        if profile.attendance_percentage < 75.0:
            risk_score += 2
            reasons.append("Low Attendance")
            
        # 4. Mock Test Performance (Average)
        avg_score = MockTestResult.objects.filter(student=user).aggregate(Avg('score'))['score__avg']
        if avg_score is not None:
             # Assuming score is percentage or normalized to 100
             if avg_score < 50:
                 risk_score += 2
                 reasons.append("Poor Mock Test Performance")
             elif avg_score < 70:
                 risk_score += 1
        else:
            risk_score += 1 # No tests taken is a slight risk
            reasons.append("No Mock Tests Taken")

        # 5. Resume Strength (Provisional)
        if profile.resume_score < 5:
            risk_score += 2
            reasons.append("Weak Resume Score")

        # 6. Skill Mismatch (Provisional)
        if profile.skill_score < 5:
             risk_score += 1
             reasons.append("Low Skill Score")
            
        # Determine Level
        if risk_score >= 8:
            level = 'High'
        elif risk_score >= 4:
            level = 'Medium'
        else:
            level = 'Low'
            
        # Update profile
        profile.placement_risk = level
        profile.save()
        
        return Response({
            'risk_level': level,
            'risk_score': risk_score,
            'factors': reasons
        })

class AdminDashboardStatsView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        total_drives = PlacementDrive.objects.count()
        active_drives = PlacementDrive.objects.filter(is_active=True).count()
        total_students = CustomUser.objects.filter(role='student').count()
        total_applications = Application.objects.count()
        
        # Risk Distribution
        high_risk = StudentProfile.objects.filter(placement_risk='High').count()
        medium_risk = StudentProfile.objects.filter(placement_risk='Medium').count()
        low_risk = StudentProfile.objects.filter(placement_risk='Low').count()
        
        # Recent Applications
        recent_apps = Application.objects.order_by('-applied_at')[:5].values(
            'student__username', 'drive__company__name', 'status', 'applied_at'
        )

        # Interview Attendance Rate
        total_profiles = StudentProfile.objects.count()
        avg_attendance = StudentProfile.objects.aggregate(Avg('attendance_percentage'))['attendance_percentage__avg'] or 0
        interview_attendance_percentage = round(avg_attendance, 2)

        # Department-wise Placement Stats
        department_stats = StudentProfile.objects.values('department').annotate(
            total_students=Count('id'),
            placed_students=Count('id', filter=models.Q(placed=True))
        )
        
        # Convert to cleaner format
        dept_data = {}
        for item in department_stats:
            dept = item['department']
            if dept:
                dept_data[dept] = {
                    'total': item['total_students'],
                    'placed': item['placed_students'],
                    'placement_rate': round((item['placed_students'] / item['total_students']) * 100, 1) if item['total_students'] > 0 else 0
                }
        
        total_placed = StudentProfile.objects.filter(placed=True).count()
        
        return Response({
            'total_drives': total_drives,
            'active_drives': active_drives,
            'total_students': total_students,
            'total_applications': total_applications,
            'total_placed': total_placed,
            'risk_distribution': {
                'High': high_risk,
                'Medium': medium_risk,
                'Low': low_risk
            },
            'recent_applications': recent_apps,
            'interview_attendance_rate': interview_attendance_percentage,
            'department_stats': dept_data
        })

class StudentRiskListView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        risk_filter = request.query_params.get('risk', None)
        
        users = CustomUser.objects.filter(role='student')
        data = []
        
        for user in users:
            if hasattr(user, 'student_profile'):
                profile = user.student_profile
                
                # Check if we should filter
                if risk_filter and profile.placement_risk != risk_filter:
                    continue
                    
                data.append({
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'risk': profile.placement_risk,
                    'cgpa': profile.cgpa,
                    'arrears': profile.arrears_count,
                    'resume_score': profile.resume_score,
                    'skill_score': profile.skill_score,
                    'attendance': profile.attendance_percentage
                })
        
        return Response(data)
