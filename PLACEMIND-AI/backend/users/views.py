from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        print(f"DEBUG: Register attempt with data: {request.data}")
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            error_msg = f"DEBUG: Register validation failed: {serializer.errors}"
            print(error_msg)
            with open('debug_log.txt', 'a') as f:
                f.write(error_msg + '\n')
        return super().create(request, *args, **kwargs)

class UserDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        if not hasattr(user, 'student_profile'):
            return Response({'error': 'Profile not found'}, status=404)
        
        profile = user.student_profile
        # Use StudentProfileSerializer to update
        from .serializers import StudentProfileSerializer
        serializer = StudentProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(UserSerializer(user).data)
        return Response(serializer.errors, status=400)

from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

# AddAllowedStudentView has been removed as validation now uses placement_csv.xlsx.
