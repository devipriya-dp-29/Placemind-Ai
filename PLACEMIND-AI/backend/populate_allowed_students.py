import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'placement_system.settings')
django.setup()

from users.models import AllowedStudent

csv_file = 'd:/Fix_it_bro_projects/dharani/backend/data/6092.xlsx'
print(f"Reading from {csv_file}")
df = pd.read_excel(csv_file)

# Clear existing rows if any
AllowedStudent.objects.all().delete()

count = 0
for index, row in df.iterrows():
    student_name = str(row.get('Candidate Full Name', '')).strip()
    roll_number = str(row.get('Roll Number', '')).strip()
    email = str(row.get('Email', '')).strip()
    
    if roll_number == 'nan' or email == 'nan' or not roll_number or not email:
        continue
        
    try:
        AllowedStudent.objects.create(
            student_name=student_name,
            roll_number=roll_number,
            email=email
        )
        count += 1
    except Exception as e:
        print(f"Error creating for roll {roll_number}: {e}")

print(f"Successfully populated DB with {count} allowed students.")
