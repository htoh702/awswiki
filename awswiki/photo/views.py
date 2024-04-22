from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from photo.serializers import photoSerializer, photo_reviewsSerializer
from photo.models import photo, photo_reviews

class photoAPI(viewsets.ModelViewSet):
    queryset = photo.objects.all()
    serializer_class = photoSerializer

class photo_reviewsAPI(viewsets.ModelViewSet):
    queryset = photo_reviews.objects.all()
    serializer_class = photo_reviewsSerializer


# Create your views here.
