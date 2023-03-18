"""
Definition of urls for Userend.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.Home),

    path('login/<slug:username>/', views.login),
    
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
