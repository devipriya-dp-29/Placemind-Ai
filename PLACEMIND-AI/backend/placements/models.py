from django.db import models
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class PlacementDrive(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='drives')
    job_role = models.CharField(max_length=255)
    description = models.TextField()
    eligibility_criteria = models.TextField(help_text="Skills, branches, etc.")
    min_cgpa = models.FloatField(default=6.0)
    allowed_branches = models.CharField(max_length=255, help_text="Comma separated list of branches")
    max_arrears = models.IntegerField(default=0)
    salary_package = models.CharField(max_length=100) # e.g. "5-7 LPA"
    deadline = models.DateTimeField()
    interview_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} - {self.job_role}"

class Application(models.Model):
    STATUS_CHOICES = (
        ('applied', 'Applied'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('selected', 'Selected'),
    )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    drive = models.ForeignKey(PlacementDrive, on_delete=models.CASCADE, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    resume = models.FileField(upload_to='application_resumes/', null=True, blank=True) # Snapshot of resume at time of application

    class Meta:
        unique_together = ('student', 'drive')

    def __str__(self):
        return f"{self.student.username} -> {self.drive}"

class MockTest(models.Model):
    title = models.CharField(max_length=255)
    drive = models.ForeignKey(PlacementDrive, on_delete=models.SET_NULL, null=True, blank=True, related_name='mock_tests')
    description = models.TextField(blank=True)
    total_marks = models.IntegerField(default=100)
    duration_minutes = models.IntegerField(default=60)
    questions = models.JSONField(default=list, help_text="List of questions with options and correctIndex")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MockTestResult(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='test_results')
    test = models.ForeignKey(MockTest, on_delete=models.CASCADE, related_name='results')
    score = models.FloatField()
    taken_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.test.title}: {self.score}"
