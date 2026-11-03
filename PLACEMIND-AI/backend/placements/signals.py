from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PlacementDrive
from users.models import CustomUser, Notification

@receiver(post_save, sender=PlacementDrive)
def notify_students_on_new_drive(sender, instance, created, **kwargs):
    if created and instance.is_active:
        # Notify all students (or filter by eligibility if needed)
        students = CustomUser.objects.filter(role='student')
        notifications = []
        for student in students:
            notifications.append(
                Notification(
                    recipient=student,
                    title=f"New Placement Drive: {instance.company.name}",
                    message=f"A new drive for {instance.job_role} has been announced. Check eligibility and apply before {instance.deadline}."
                )
            )
        Notification.objects.bulk_create(notifications)
