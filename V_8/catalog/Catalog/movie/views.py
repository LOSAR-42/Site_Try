from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Articles_createForm
from .models import Articles_create

#связанно с urls.py
def catalog(request):
    movie = Articles_create.objects.all()
    return render(request, 'movie/catalog.html', {'movie': movie})

def create(request):
    error = ''
    #проверка формы на правильность
    if request.method == 'POST':
        form = Articles_createForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
        else:
            error = 'Форма была не верной'

    form = Articles_createForm()
    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'movie/create.html', data)
