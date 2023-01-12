from django.db import models

class Articles_create(models.Model):
    title = models.CharField('Название фильма', max_length=30)
    rating = models.CharField('Рейтинг Кинопоиск', max_length=30)
    description = models.TextField('Описание')
    date = models.DateField(blank=True, null=True)
    file = models.CharField('изображение', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'