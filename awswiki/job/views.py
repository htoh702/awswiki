from rest_framework import viewsets
from .serializers import JobSerializer, JobReviewSerializer
from .models import Job, JobReview

class JobAPI(viewsets.ModelViewSet):
    queryset = Job.objects.prefetch_related('reviews').all()
    serializer_class = JobSerializer

class JobReviewsAPI(viewsets.ModelViewSet):
    queryset = JobReview.objects.all()
    serializer_class = JobReviewSerializer
