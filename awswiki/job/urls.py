from django.urls import path,include

from .views import JobAPI, Job_reviewsAPI
from rest_framework import routers

job_router = routers.DefaultRouter()
job_router.register(r'api', JobAPI, basename="Job_api")

job_reviews_router = routers.DefaultRouter()
job_reviews_router.register(r'api', Job_reviewsAPI, basename="Job_api_reviews")


urlpatterns = [
    path('', include(job_router.urls)),
    path('reviews/', include(job_reviews_router.urls))
]