from rest_framework import serializers
from .models import photo_reviews, photo

class photoSerializer(serializers.ModelSerializer):
    class Meta :
        model = photo
        fields = '__all__'

class photo_reviewsSerializer(serializers.ModelSerializer):
    class Meta :
        model = photo_reviews
        fields = '__all__'