import os
import django
import sys

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'placement_system.settings')
django.setup()

from users.models import CustomUser
from placements.models import Company
from analytics.ml_models import predictor

def check_backend():
    print("Checking Django environment...")
    try:
        user_count = CustomUser.objects.count()
        print(f"User count: {user_count}")
        
        company_count = Company.objects.count()
        print(f"Company count: {company_count}")
        
        print("Checking ML Predictor...")
        risk, prob = predictor.predict_risk(8.5, 0, 80, 2)
        print(f"Prediction test (8.5 CGPA): {risk}")
        
        print("Backend setup check: SUCCESS")
    except Exception as e:
        print(f"Backend setup check: FAILED - {e}")

if __name__ == "__main__":
    check_backend()
