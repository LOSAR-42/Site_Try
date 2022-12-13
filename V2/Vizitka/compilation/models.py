from django.db import models

#связанно с forms.py
class Movies(models.Model):
    # максимально 250 символов
    title = models.CharField('Название', max_length=50) #default='Не указанно: название фильма')
    genre = models.CharField('Название', max_length=70) #default='Не указанно: Жанр фильма')
    # тут побольше
    description = models.TextField('Описание')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'