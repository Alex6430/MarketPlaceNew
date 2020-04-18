from django.conf.urls import url, include
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    path('admin/', views.admin, name='admin'),
]
