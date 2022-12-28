from django.shortcuts import render
from django.http import HttpResponse

#связанно с urls.py
def basic(request):
    return render(request, 'main/basic.html')

def contact (request):
    return render(request, 'main/contact.html')
