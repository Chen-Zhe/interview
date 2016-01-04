from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    USER_TYPE = (
        ('hr', 'HR manager'),
        ('er', 'Interviewer'),
        ('ee', 'Interviewee'),
    )

    user = models.OneToOneField(User, related_name="profile")
    type = models.CharField(max_length=1, choices=USER_TYPE)

class Organization(models.Model):
    name = models.CharField(max_length=50)
    max_position = models.IntegerField()
    manager = models.ForeignKey(User, related_name="organization")

class Portfolio(models.Model):
    organization = models.ForeignKey(Organization, related_name="portfolio")
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    number_of_position = models.IntegerField()