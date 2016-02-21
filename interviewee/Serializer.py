import  django.contrib.auth.models
import rest_framework.serializers
import interviewee.models


class IntervieweeSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = interviewee.models.Interviewee
        fields = '__all__'