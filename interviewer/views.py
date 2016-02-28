from django.shortcuts import render
from interviewee.models import *
from interviewer.models import *
from hrm.models import *


# first interface of the interviewer system
def portfolio_selection(request):
    portfolios = Portfolio.objects.all()
    return render(request,"port_sel.html", {'portfolios':portfolios})


def all_applications(request, port_id):
    applications = Portfolio.objects.get(id=port_id).applications
    return render(request,"application_sel.html", {'applications':applications})

def calling_applicant(request, application_id):
    pass