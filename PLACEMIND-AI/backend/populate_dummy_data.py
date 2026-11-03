import os
import django
import sys

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'placement_system.settings')
django.setup()

from placements.models import Company, PlacementDrive
from django.utils import timezone
from datetime import timedelta

def populate_data():
    print("Populating dummy data...")

    # Create Companies
    companies_data = [
        {"name": "Google", "description": "Tech Giant", "website": "https://google.com"},
        {"name": "Microsoft", "description": "Tech Giant", "website": "https://microsoft.com"},
        {"name": "Amazon", "description": "E-commerce & Cloud", "website": "https://amazon.com"},
        {"name": "TCS", "description": "IT Services", "website": "https://tcs.com"},
        {"name": "Infosys", "description": "IT Services", "website": "https://infosys.com"},
    ]

    for data in companies_data:
        company, created = Company.objects.get_or_create(
            name=data['name'],
            defaults={
                "description": data['description'],
                "website": data['website']
            }
        )
        if created:
            print(f"Created company: {company.name}")
        else:
            print(f"Company {company.name} already exists")

    # Create a dummy drive if none exist
    if not PlacementDrive.objects.exists():
        company = Company.objects.first()
        PlacementDrive.objects.create(
            company=company,
            job_role="Software Engineer",
            description="Backend Developer role",
            eligibility_criteria="B.Tech CSE/IT",
            min_cgpa=7.5,
            allowed_branches="CSE, IT",
            max_arrears=0,
            salary_package="12 LPA",
            deadline=timezone.now() + timedelta(days=10),
            interview_date=timezone.now() + timedelta(days=15),
            is_active=True
        )
        print("Created dummy Placement Drive")
    else:
        print("Placement Drives already exist")

    # Create Dummy Mock Test
    from placements.models import MockTest
    if not MockTest.objects.exists():
        questions = [
            {
                "id": 1,
                "question": "If a train travels 60 km in 1 hour, what is its speed?",
                "options": ["50 km/h", "60 km/h", "70 km/h", "80 km/h"],
                "correctIndex": 1
            },
            {
                "id": 2,
                "question": "What comes next in the series: 2, 4, 8, 16, ...?",
                "options": ["30", "32", "24", "18"],
                "correctIndex": 1
            },
             {
                "id": 3,
                "question": "Find the odd one out: Apple, Banana, Carrot, Date",
                "options": ["Apple", "Banana", "Carrot", "Date"],
                "correctIndex": 2
            }
        ]
        MockTest.objects.create(
            title="General Aptitude Test 1",
            description="A comprehensive test covering logical reasoning and quantitative aptitude.",
            total_marks=20,
            duration_minutes=30,
            questions=questions
        )
        print("Created dummy Mock Test")
    else:
        print("Mock Tests already exist")

    # Create Dummy Notifications for existing users
    from users.models import CustomUser, Notification
    user = CustomUser.objects.first()
    if user:
        if not Notification.objects.filter(recipient=user).exists():
            Notification.objects.create(
                recipient=user,
                title="Welcome to Placement Portal",
                message="Your profile has been successfully created. Complete your details to apply for drives."
            )
            Notification.objects.create(
                recipient=user,
                title="New Drive Alert",
                message="Google is hiring for Software Engineer role. Check it out!"
            )
            print(f"Created dummy notifications for user: {user.username}")
        else:
            print("Notifications already exist for user")

    print("Data population complete.")

if __name__ == "__main__":
    populate_data()
