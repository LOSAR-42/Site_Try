from django.shortcuts import render, redirect
from .models import Movies
from .forms import MoviesForm
from django.views.generic import DetailView, UpdateView


def compilation_home(request):
    movie = Movies.objects.order_by('-date')
    return render(request, 'compilation/compilation_home.html', {'movie':movie})

class Movie_Detail(DetailView):
    model = Movies
    template_name = 'compilation/detail_movie.html'
    context_object_name = 'movie_det'


def create(request):
    error = ''
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Не верный ввод данных'

    form = MoviesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'compilation/create.html', data)