from django.urls import path,include

from .views import PhotoAPI
from rest_framework import routers

photo_router = routers.DefaultRouter()
photo_router.register(r'api', PhotoAPI, basename="photo_post")


urlpatterns = [
    path('', include(photo_router.urls)),
]