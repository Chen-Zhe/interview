from django.shortcuts iutil_namemport render, redirect, HttpResponse
from interviewee.models import *
from hrm.models import *


# first interface of the interviewer system
def portfolio_selection(request):
    portfolios = Portfolio.objects.all()
    return render(request,"port_sel.html", {'portfolios':portfolios})

def all_applications(request, port_id):
    applications = Portfolio.objects.get(id=port_id).applications
    return render(request,"application_sel.html", {'applications':applications})

def calling_applicant(request, application_id):
    application=InterviewApplication.objects.get(id=application_id)
    QueueList(1,application.portfolio.name, application.interviewee.name).save()
    return render(request,"calling_applicant.html", {"application": application})

def interview_action(request, application_id, action):
    application = InterviewApplication.objects.get(id=application_id)
    port_id=application.portfolio.id

    if action == "cancel":
        QueueList.objects.get(organization=1,portfolio=application.portfolio.name, interviewee=application.interviewee.name).delete()
        return redirect("/interview/port/"+str(port_id)+"/")
    elif action == "interview":
        if request.method == 'POST':
            application.interviewer_comments = request.POST["comments"]
            application.save()
            return redirect("/interview/port/"+str(port_id)+"/")
        else:
            QueueList.objects.get(organization=1,portfolio=application.portfolio.name, interviewee=application.interviewee.name).delete()
            return render(request, 'interviewing.html', {'application': application})


    #default return
    return HttpResponse("<h1>Error!</h1>")
