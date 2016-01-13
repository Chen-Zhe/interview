from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    USER_TYPE = (
        ('hr', 'HR manager'),
        ('er', 'Interviewer'),
        ('ee', 'Interviewee'),
    )

    user = models.OneToOneField(User, related_name="profile")
    type = models.CharField(max_length=2, choices=USER_TYPE)
    preferred_name = models.CharField(max_length=100)

class Organization(models.Model):
    name = models.CharField(max_length=50)
    manager = models.ForeignKey(User, related_name="organization")
    application_limit = models.IntegerField() # limit of application per person
    ongoing_interview = models.BooleanField()

class Portfolio(models.Model):
    organization = models.ForeignKey(Organization, related_name="portfolio")
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    number_of_position = models.IntegerField()

class QueueList(models.Model):
    organization = models.ForeignKey(Organization, related_name='current_queue')
    portfolio = models.CharField(max_length=50)
    interviewee = models.CharField(max_length=100)