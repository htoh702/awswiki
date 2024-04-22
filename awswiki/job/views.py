from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from job.serializers import jobSerializer, job_reviewsSerializer
from job.models import job, job_reviews

class JobAPI(viewsets.ModelViewSet):
    queryset = job.objects.all()
    serializer_class = jobSerializer

class Job_reviewsAPI(viewsets.ModelViewSet):
    queryset = job_reviews.objects.all()
    serializer_class = job_reviewsSerializer


# Create your views here.
