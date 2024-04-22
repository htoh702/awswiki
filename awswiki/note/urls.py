from django.urls import path,include

from .views import NoteAPI
from rest_framework import routers

note_router = routers.DefaultRouter()
note_router.register(r'api', NoteAPI, basename="Not_api")


urlpatterns = [
    path('', include(note_router.urls)),
]