from rest_framework import serializers
from .models import CustomUser, StudentProfile

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['degree', 'cgpa', 'department', 'year_of_study', 'skills', 'placed', 'resume', 
                  'arrears_count', 'attendance_percentage', 'missed_interviews_count', 'placement_risk',
                  'resume_score', 'skill_score']

class UserSerializer(serializers.ModelSerializer):
    student_profile = StudentProfileSerializer(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'student_profile']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(read_only=True) # Default to student for public registration
    first_name = serializers.CharField(required=True)
    
    # Profile fields
    degree = serializers.CharField(required=False, allow_blank=True)
    department = serializers.CharField(required=False, allow_blank=True)
    cgpa = serializers.FloatField(required=False, default=0.0)
    year_of_study = serializers.IntegerField(required=False, default=1)
    arrears_count = serializers.IntegerField(required=False, default=0)
    skills = serializers.CharField(required=False, allow_blank=True)
    resume = serializers.FileField(required=False)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role', 'first_name',
                  'degree', 'department', 'cgpa', 'year_of_study', 'arrears_count', 'skills', 'resume']
    
    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        resume = data.get('resume')
        first_name = data.get('first_name', '')
        
        if not resume:
            raise serializers.ValidationError({"resume": "Resume upload is mandatory for registration."})
            
        allowed_extensions = ['.pdf', '.doc', '.docx']
        ext = str(resume.name).lower()
        if not any(ext.endswith(ext_str) for ext_str in allowed_extensions):
            raise serializers.ValidationError({"resume": "Only PDF, DOC, and DOCX formats are allowed."})
            
        from .models import AllowedStudent
        
        input_roll = str(username).strip()
        input_email = str(email).strip()
        input_name = str(first_name).strip()
        
        student = AllowedStudent.objects.filter(roll_number=input_roll, email__iexact=input_email).first()
        
        if not student:
            raise serializers.ValidationError({"non_field_errors": ["Your Roll Number and/or Email do not match our authorized records. Please check your details."]})
            
        if input_name and student.student_name:
            if student.student_name.lower() != input_name.lower():
                raise serializers.ValidationError({"non_field_errors": [f"Student Name '{input_name}' does not match the authorized records '{student.student_name}'. Please check with admin."]})
            
        return data
        
    def create(self, validated_data):
        # Extract profile data
        import random
        profile_data = {
            'degree': validated_data.pop('degree', ''),
            'department': validated_data.pop('department', ''),
            'cgpa': validated_data.pop('cgpa', 0.0),
            'year_of_study': validated_data.pop('year_of_study', 1),
            'arrears_count': validated_data.pop('arrears_count', 0),
            'skills': validated_data.pop('skills', ''),
            'resume': validated_data.pop('resume', None),
            'resume_score': random.randint(6, 9),
            'skill_score': random.randint(6, 9)
        }

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            role='student'
        )
        
        # Create profile with data
        StudentProfile.objects.create(user=user, **profile_data)
        return user

from .models import Notification
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

