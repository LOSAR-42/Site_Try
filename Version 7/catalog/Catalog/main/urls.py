from django.urls import path
from . import views

#связанно с views.py
urlpatterns = [
    path('', views.basic, name="home"),
    path('contact', views.contact, name="contact"),
]
