from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=50, blank=True)  # e.g. "3-4 LPA"
    posted_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # Structured fields for LinkedIn-style JD
    about = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)
    must_have_skills = models.TextField(blank=True)
    good_to_have_skills = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
    benefits = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('shortlisted', 'ShortListed'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} applied for {self.job.title}"
