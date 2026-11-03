import os
import django
import sys

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'placement_system.settings')
django.setup()

from users.models import CustomUser, StudentProfile

def update_latest_student_cgpa():
    # Get the most recently joined student
    try:
        latest_student = CustomUser.objects.filter(role='student').latest('date_joined')
        profile = latest_student.student_profile
        
        print(f"Updating CGPA for user: {latest_student.username}")
        print(f"Old CGPA: {profile.cgpa}")
        
        profile.cgpa = 8.5
        profile.save()
        
        print(f"New CGPA: {profile.cgpa}")
        print("Update complete. You should now be eligible for drives requiring up to 8.5 CGPA.")
        
    except CustomUser.DoesNotExist:
        print("No student users found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_latest_student_cgpa()
