from django.urls import path,include

from .views import photoAPI, photo_reviewsAPI
from rest_framework import routers

photo_router = routers.DefaultRouter()
photo_router.register(r'api', photoAPI, basename="photo_api")

photo_reviews_router = routers.DefaultRouter()
photo_reviews_router.register(r'api', photo_reviewsAPI, basename="photo_api_reviews")


urlpatterns = [
    path('', include(photo_router.urls)),
    path('reviews/', include(photo_reviews_router.urls))
]