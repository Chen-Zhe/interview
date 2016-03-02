from django.conf.urls import url
import interviewee.views


urlpatterns = [
    url(r'^reg/',interviewee.views.RegisterViewSet.as_view()),
    url(r'^login/',interviewee.views.LoginViewSet.as_view()),
    url(r'^test/',interviewee.views.Test.as_view())
]