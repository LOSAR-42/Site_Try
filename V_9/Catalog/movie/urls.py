from django.urls import path
from . import views

#связанно с views.py
urlpatterns = [
    path('', views.catalog, name="catalog"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.MovieDetailView.as_view(), name="movie_detail"),
]
