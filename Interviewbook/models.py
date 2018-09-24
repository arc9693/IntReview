from django.db import models
from django.utils import timezone


class InterviewResponse(models.Model):
    company = models.CharField(max_length=200)
    job_profile = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    rounds = models.IntegerField(blank=True, null=True)
    questions = models.CharField(max_length=5000)
    compensation = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company
