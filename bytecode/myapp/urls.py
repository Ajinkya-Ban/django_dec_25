from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("home/", views.Home_Page_View)
]