from .models import Movies
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

#связанно с models.py
class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = ['title', 'genre', 'description', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название фильма'
            }),
            "genre": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Жанр'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control'
            })
        }
