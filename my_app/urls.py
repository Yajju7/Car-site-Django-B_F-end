"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django import views
from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'my_app'



urlpatterns = [
    path('',views.home_page, name = 'home'),
    path('vari/',views.vari, name = 'vari'),
    path('links/',views.links, name = 'links'),
    path('lists/',views.list_patient, name='patient-list'),
    
]





