from django.urls import path,include

from .views import noteAPI, note_reviewsAPI
from rest_framework import routers

note_router = routers.DefaultRouter()
note_router.register(r'api', noteAPI, basename="note_api")

note_reviews_router = routers.DefaultRouter()
note_reviews_router.register(r'api', note_reviewsAPI, basename="note_api_reviews")


urlpatterns = [
    path('', include(note_router.urls)),
    path('reviews/', include(note_reviews_router.urls))
]