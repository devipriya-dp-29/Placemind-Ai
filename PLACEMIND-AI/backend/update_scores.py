import os
import django
import sys
import random

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'placement_system.settings')
django.setup()

from users.models import StudentProfile

def update_scores():
    profiles = StudentProfile.objects.all()
    count = 0
    for profile in profiles:
        # Give random realistic scores out of 10
        profile.resume_score = random.randint(6, 9)
        profile.skill_score = random.randint(6, 9)
        profile.save()
        count += 1
        
    print(f"Updated skill and resume scores for {count} students.")

if __name__ == "__main__":
    update_scores()
