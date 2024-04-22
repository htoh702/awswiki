from django.urls import path,include

from .views import JobAPI
from rest_framework import routers

job_router = routers.DefaultRouter()
job_router.register(r'api', JobAPI, basename="Job_api")


urlpatterns = [
    path('', include(job_router.urls)),
]