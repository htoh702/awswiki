from rest_framework import serializers
from .models import Job, JobReview

class JobReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobReview
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    reviews = JobReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
