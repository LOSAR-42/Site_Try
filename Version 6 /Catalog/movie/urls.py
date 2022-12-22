from django.urls import path
from . import views

#связанно с views.py
urlpatterns = [
    path('', views.catalog, name="catalog"),
]
