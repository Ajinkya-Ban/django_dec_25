from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("home/", views.Home_Page_View, name="home"),
    path("about/", views.About_Page_View, name="about"),
    path("contact/", views.Contact_Page_View, name="contact")
]