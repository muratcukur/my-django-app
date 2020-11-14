
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import GeneralInformation_View
from . import views

urlpatterns = [
    url('index/',views.GeneralInformation_View,name="GeneralInformation_View"),
  

    
]
