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

class searchSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    tag = serializers.CharField()
    title = serializers.CharField(required=False)
    writer = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    date = serializers.DateTimeField()
    image = serializers.FileField()