import  django.contrib.auth.models
import rest_framework.serializers
import interviewee.models


class IntervieweeSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = interviewee.models.Interviewee
        fields = '__all__'


class UserSerializer(rest_framework.serializers.ModelSerializer):
    Email = rest_framework.serializers.CharField(
        style = {'placeholder' : 'Email'},
        source= 'username'
    )
    password = rest_framework.serializers.CharField(
        style = {'placeholder' : 'Password1',
                 'input_type': 'password'},
    )

    class Meta:
        model = django.contrib.auth.models.User
        fields = ['Email', 'password']


class RegistrationSerializer(rest_framework.serializers.ModelSerializer):


    name = rest_framework.serializers.CharField(
        max_length=20,
        style= {'placeholder': 'Bertil Andersson'}
    )

    matric_no = rest_framework.serializers.CharField(
        max_length=9,
        style= {'placeholder': 'U1234567A'}
    )

    study_major = rest_framework.serializers.CharField(
        style={'placeholder' : 'EEE'}
    )

    study_year = rest_framework.serializers.IntegerField(
        style={'placeholder' : '3'}
    )

    phone = rest_framework.serializers.IntegerField(
        style={'placeholder' : '98765432'}
    )

    email = rest_framework.serializers.EmailField(
        source = "user.username",
         max_length=20,
        style={'placeholder': 'your Email@e.ntu.edu.sg'}
    )
    password = rest_framework.serializers.CharField(
        source = "user.password",
         max_length=20,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = interviewee.models.Interviewee
        field = ['name',
                 'matric_no',
                 'study_year',
                 'study_major',
                 'phone'
                 'email',
                 'password',
                 ]
        exclude = ('user',)

    def is_valid(self, raise_exception=False):
        error = super(RegistrationSerializer, self).is_valid(raise_exception = raise_exception)
        try:
            django.contrib.auth.models.User.objects.get(username=self.initial_data['email'])
        except django.contrib.auth.models.User.DoesNotExist:
            return error
        if self._errors:
            self._errors['email'].append('This email is already registered')
        else:
            self._errors = {'email' :['This email is already registered']}
        return False

    def create(self, validated_data):
        info = validated_data.pop('user')
        print(info)
        user = django.contrib.auth.models.User.objects.create_user(
            username = info.get('username'),
            email = info.get('username'),
            password = info.get('password'))
        validated_data['user']= user
        return super(RegistrationSerializer, self).create(validated_data)