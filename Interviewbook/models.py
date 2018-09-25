from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class InterviewResponse(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    job_profile = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    rounds = models.IntegerField(blank=True, null=True)
    questions = models.CharField(max_length=5000)
    compensation = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company
