from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from note.serializers import noteSerializer, note_reviewsSerializer
from note.models import note, note_reviews

class noteAPI(viewsets.ModelViewSet):
    queryset = note.objects.all()
    serializer_class = noteSerializer

class note_reviewsAPI(viewsets.ModelViewSet):
    queryset = note_reviews.objects.all()
    serializer_class = note_reviewsSerializer


# Create your views here.
