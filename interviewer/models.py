from django.db import models
from django.contrib.auth.models import User
from hrm.models import Portfolio

class InterviewAssignment(models.Model):
    interviewer = models.ForeignKey(User)
    portfolio = models.ForeignKey(Portfolio, related_name="interviewers_assignment")