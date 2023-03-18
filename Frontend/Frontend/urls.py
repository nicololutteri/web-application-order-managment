"""
Definition of urls for Frontend.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),
    
    path('orders/', views.orders, name='orders'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('loginInfo/', views.logininfo, name='loginInfo'),
    
    path('admin/', admin.site.urls),
]
