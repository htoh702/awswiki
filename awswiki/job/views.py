from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from job.serializers import jobSerializer, job_reviewsSerializer, searchSerializer
from job.models import job, job_reviews

from note.models import note
from photo.models import photo

class JobAPI(viewsets.ModelViewSet):
    queryset = job.objects.all()
    serializer_class = jobSerializer

    @action(detail=False, methods=['get'])
    def AllSearch(self, request):
        search = request.query_params.get('search')
        if not search:
            return Response("Search parameter 'search' is required.", status=status.HTTP_400_BAD_REQUEST)

        job_results = job.objects.filter(tag__icontains=search) | job.objects.filter(title__icontains=search) | job.objects.filter(content__icontains=search)
        note_results = note.objects.filter(tag__icontains=search) | note.objects.filter(title__icontains=search) | note.objects.filter(content__icontains=search)
        photo_results = photo.objects.filter(tag__icontains=search)

        search_results = list(job_results) + list(note_results) + list(photo_results)

        serializer = searchSerializer(search_results, many=True)

        return Response(serializer.data)

class Job_reviewsAPI(viewsets.ModelViewSet):
    queryset = job_reviews.objects.all()
    serializer_class = job_reviewsSerializer


# Create your views here.
