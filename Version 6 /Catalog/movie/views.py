from django.shortcuts import render
from django.http import HttpResponse

#связанно с urls.py
def catalog(request):
    return render(request, 'movie/catalog.html')
