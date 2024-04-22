from rest_framework import serializers
from .models import note_reviews, note

class noteSerializer(serializers.ModelSerializer):
    class Meta :
        model = note
        fields = '__all__'

class note_reviewsSerializer(serializers.ModelSerializer):
    class Meta :
        model = note_reviews
        fields = '__all__'