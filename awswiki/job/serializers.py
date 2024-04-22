from rest_framework import serializers
from .models import job_reviews, job

class jobSerializer(serializers.ModelSerializer):
    class Meta :
        model = job
        fields = '__all__'

class job_reviewsSerializer(serializers.ModelSerializer):
    class Meta :
        model = job_reviews
        fields = '__all__'