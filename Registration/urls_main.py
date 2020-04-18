from django.conf.urls import url, include
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    path('auth/login', views.auth_login, name='login'),
    path('auth/logout', views.auth_logout, name='logout'),
    path('admin/', views.admin, name='admin'),
    path('reg/', views.reg, name='registration'),
    # path('home/', views.account_view, name='home'),
    path('', views.index, name='index'),
]
