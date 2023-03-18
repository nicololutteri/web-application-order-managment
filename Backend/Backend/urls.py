"""
Definition of urls for Userend.
"""

from app import forms, views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.Home),

    path('orders/all/', views.clientAllOrders),
    path('orders/', views.getOrder),
    path('orders/<int:code>/', views.getOrder),

    path('clients/<slug:code>/', views.clientInfo),
    path('agents/<slug:code>/', views.agentInfo),
]

urlpatterns = format_suffix_patterns(urlpatterns)
