from django.shortcuts import render
from rest_framework import viewsets,mixins
from interviewee.models import *
from interviewee.Serializer import IntervieweeSerializer,UserSerializer
from rest_framework import generics
import interviewee.Serializer
from django.contrib.auth import *

class IntervieweeViewSet(viewsets.ModelViewSet):
    queryset = Interviewee.objects.all()
    serializer_class = IntervieweeSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterViewSet(mixins.CreateModelMixin
                        ,generics.GenericAPIView):
    queryset = Interviewee.objects.all()
    serializer_class = interviewee.Serializer.RegistrationSerializer



    def get(self, request):

        return render(request,'register.html', {'serializer': self.serializer_class,
                         'title' : 'Register for Interview'})
        # return Response({'serializer': self.serializer_class,
        #                  'title' : 'Register for Interview'},
        #                 template_name='register.html',
        #                 re)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return render(request,'register.html',{'serializer': serializer,
                         'title' : 'Register for Interview'})
        self.create(request,*args,**kwargs)
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request,user)
        return render(request,'success.html',{'message': 'Registation successful'})


class LoginViewSet(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self,request):
        return render(request, 'login.html', {'serializer': self.serializer_class})

    def post(self, request):
        username = request.POST['Email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'success.html', {'message': 'Logged in'})
            else:
                pass
        else:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid()
            return render(request, 'login.html', {'serializer': serializer})


class Test(generics.GenericAPIView):

    def get(self, request ):
        return render(request,'register2.html')