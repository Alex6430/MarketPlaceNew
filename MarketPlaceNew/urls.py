"""MarketPlaceNew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url , include
from django.urls import path
from Market import urls_market, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.account_view, name='home'),
    path('take_delivery/<id_request>', views.take_delivery, name='take_delivery'),
    path('delivery/<id_request>', views.delivery, name='delivery'),
    path('update_status/<id_request>', views.update_status, name='update_status'),
    path('down_status/<id_request>', views.down_status, name='down_status'),
    path('manager_request/', views.manager_request, name='manager_request'),
    path('manager_product/', views.manager_product, name='manager_product'),
    path('', include('Registration.urls_main')),
]
