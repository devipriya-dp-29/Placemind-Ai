from django.contrib import admin
from .models import CustomUser, StudentProfile, Notification, AllowedStudent

admin.site.register(CustomUser)
admin.site.register(StudentProfile)
admin.site.register(Notification)
admin.site.register(AllowedStudent)
