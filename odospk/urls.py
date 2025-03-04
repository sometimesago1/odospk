from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('landing.urls')),
    #Autorealoding agent urls
    path("__reload__/", include("django_browser_reload.urls")),
]
