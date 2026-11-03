from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    
    def __str__(self):
        return self.username

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    degree = models.CharField(max_length=100, blank=True) # e.g. B.Tech, M.Tech
    cgpa = models.FloatField(default=0.0)
    department = models.CharField(max_length=100)
    year_of_study = models.IntegerField(default=1)
    skills = models.TextField(blank=True) # Comma separated
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    placed = models.BooleanField(default=False)
    
    # New fields for risk analysis and monitoring
    arrears_count = models.IntegerField(default=0)
    attendance_percentage = models.FloatField(default=100.0)
    missed_interviews_count = models.IntegerField(default=0)
    resume_score = models.IntegerField(default=0) # Score out of 10
    skill_score = models.IntegerField(default=0) # Score based on skills count/relevance
    placement_risk = models.CharField(max_length=20, default='Low') # Low, Medium, High
    warning_issued = models.BooleanField(default=False)
    account_frozen = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Notification for {self.recipient.username}: {self.title}"

class AllowedStudent(models.Model):
    student_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=50, unique=True, help_text="Used as username")
    
    def __str__(self):
        return f"{self.roll_number} - {self.email}"
