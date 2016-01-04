from django.db import models
from django.contrib.auth.models import User
from hrm.models import Portfolio

class Interviewee(models.Model):
    user = models.ForeignKey(User,related_name="interviewee")
    preferred_name = models.CharField(max_length=50)
    birthday = models.DateField()

class InterviewApplication(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name="applications")
    Interviewee = models.ForeignKey(Interviewee)
    study_year = models.IntegerField()
    study_major = models.CharField(max_length=50)