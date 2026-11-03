import os
import django
import sys
from django.conf import settings

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'placement_system.settings')
django.setup()

from placements.models import Company

def verify_data():
    print(f"Using Database: {settings.DATABASES['default']['NAME']}")
    print(f"Host: {settings.DATABASES['default']['HOST']}")
    
    count = Company.objects.count()
    print(f"Company Count: {count}")
    
    if count > 0:
        for c in Company.objects.all():
            print(f"- {c.name} (ID: {c.id})")
    else:
        print("No companies found!")

if __name__ == "__main__":
    verify_data()
