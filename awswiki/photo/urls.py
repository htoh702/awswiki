from django.urls import path,include

from .views import TravelAPI
from rest_framework import routers

travel_router = routers.DefaultRouter()
travel_router.register(r'api', TravelAPI, basename="cafe_post")


urlpatterns = [
    path('', include(travel_router.urls)),
]