from django.urls import path
from . import views

# связанно с views.py
urlpatterns = [
    path('', views.compilation_home, name='compilation_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.Movie_Detail.as_view(), name='compilation_detail'),
]
