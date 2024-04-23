from rest_framework import viewsets
from .serializers import NoteSerializer, NoteReviewSerializer
from .models import Note, NoteReview

class NoteAPI(viewsets.ModelViewSet):
    queryset = Note.objects.prefetch_related('reviews').all()
    serializer_class = NoteSerializer

class NoteReviewsAPI(viewsets.ModelViewSet):
    queryset = NoteReview.objects.all()
    serializer_class = NoteReviewSerializer
