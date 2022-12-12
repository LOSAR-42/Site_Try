from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ["v1","v2","v3" ],
        'obt': {
            'movie': 'horror',
            'anime': 'isekai',
            'something': 'else',
        }
    }
    return render(request, 'main/index.html', data)



def about(request):
    return render(request, 'main/about.html', {'title': 'Обо мне'})
