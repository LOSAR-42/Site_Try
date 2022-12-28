from .models import Articles_create
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, DateField
from django import forms

class Articles_createForm(ModelForm):
    class Meta:
        model = Articles_create
        fields = ['title', 'rating', 'description', 'date', 'file']

        widgets = {
            "title": TextInput(attrs={
                'class': 'forms_create',
                'placeholder': 'Название фильма',
            }),
            "rating": TextInput(attrs={
                'class': 'forms_create',
                'placeholder': 'Рейтинг',
            }),
            "description": Textarea(attrs={
                'class': 'textarea_description',
                'placeholder': 'Описание',
            }),
            "date": DateTimeInput(attrs={
                'class': 'forms_create',
                'placeholder': 'ДД.ММ.ГГ (10.12.2013)',
            }),
            "file": TextInput(attrs={
                'class': 'forms_create',
                'placeholder': 'Изображение',
            }),
        }