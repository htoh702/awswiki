from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

class NoteAPI(viewsets.ModelViewSet):
    queryset = 0

# Create your views here.
