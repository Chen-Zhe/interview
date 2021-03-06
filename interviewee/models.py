from django.db import models
from django.contrib.auth.models import User
from hrm.models import Portfolio


class Interviewee(models.Model):
    user = models.ForeignKey(User,related_name="interviewee")
    matric_no = models.CharField(max_length=9)
    name = models.CharField(max_length=50)
    study_year = models.IntegerField()
    study_major = models.CharField(max_length=50)
    phone = models.IntegerField()

class InterviewApplication(models.Model):
    STATUS = (
        ('n', 'NIL'),
        ('i', 'interviewed'),
        ('a', 'absent'),
        ('d', 'done'), #done
        # ('r', 'Offer Rejected'),
        # ('a', 'Offer Accepted'),
    )

    portfolio = models.ForeignKey(Portfolio, related_name="applications")
    interviewee = models.ForeignKey(Interviewee)
    reason = models.CharField(max_length=500) # write up
    Interviewee = models.ForeignKey(Interviewee,related_name="interviewee")
    reason = models.CharField(max_length=500)  # write up

    interviewer_comments = models.CharField(max_length=500)
    short_listed = models.BooleanField()
    type = models.CharField(max_length=1, choices=STATUS, default='n')
