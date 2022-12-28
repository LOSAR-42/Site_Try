from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    #странциа URL='about', импортированно из views.py, название(видимо) = about
    path('about', views.about, name='about')
]