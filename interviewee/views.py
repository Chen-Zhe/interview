from django.shortcuts import render
from rest_framework import viewsets
from interviewee.models import *
from interviewee.Serializer import IntervieweeSerializer

class IntervieweeViewSet(viewsets.ModelViewSet):
    queryset = Interviewee.objects.all()
    serializer_class = IntervieweeSerializer