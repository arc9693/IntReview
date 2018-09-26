from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class InterviewResponse(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    job_profile = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    rounds = models.IntegerField(blank=True, null=True)
    questions = models.CharField(max_length=100000)
    compensation = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    hits=models.IntegerField(default=0)

    def __str__(self):
        return str(self.company)

    def increase(self):
        self.hits += 1
        self.save()
