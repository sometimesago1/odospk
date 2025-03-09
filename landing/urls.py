from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePage.as_view(), name='home'),
    path("directions/", DirectionsPage.as_view(), name="directions"),
    path('courses/', CoursesPage.as_view(), name='courses'),
]
