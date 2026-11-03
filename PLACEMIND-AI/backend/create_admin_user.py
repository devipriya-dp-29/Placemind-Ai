import os
import django
import sys

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'placement_system.settings')
django.setup()

from users.models import CustomUser

def create_admin():
    username = 'admin'
    password = 'adminpassword'
    email = 'admin@example.com'

    if not CustomUser.objects.filter(username=username).exists():
        print(f"Creating admin user: {username}")
        user = CustomUser.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            role='admin'
        )
        print(f"Admin user created successfully.")
        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        print(f"Admin user '{username}' already exists.")
        # Ensure role is admin
        user = CustomUser.objects.get(username=username)
        if user.role != 'admin':
            user.role = 'admin'
            user.save()
            print(f"Updated '{username}' role to 'admin'.")

if __name__ == "__main__":
    create_admin()
