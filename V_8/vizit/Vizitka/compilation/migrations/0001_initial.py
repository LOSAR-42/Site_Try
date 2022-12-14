# Generated by Django 4.1.3 on 2022-12-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Не указанно: название фильма', max_length=50, verbose_name='Название')),
                ('genre', models.CharField(default='Не указанно: Жанр фильма', max_length=70, verbose_name='Название')),
                ('description', models.TextField(default='Не указано: описание', verbose_name='Описание')),
                ('date', models.DateField(verbose_name='Дата публикации')),
            ],
        ),
    ]
