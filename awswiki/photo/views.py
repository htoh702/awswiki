from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from .models import Photo
from .serializers import PhotoSerializer

class PhotoAPI(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDateAPI(APIView):
    def get(self, request, date, format=None):
        photos = Photo.objects.filter(date__date=date)
        if not photos.exists():
            return Response({"message": "No photos found for this date"}, status=404)
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)
