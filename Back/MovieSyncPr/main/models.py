from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Films(models.Model):
    title = models.CharField('Название фильма',max_length=150)
    description = models.CharField('Описание фильма', max_length=350)
    picture = models.ImageField(upload_to='')
    genres = models.ManyToManyField(Genre, related_name='films', blank=True)
    favorites = models.ManyToManyField(User, related_name='favorite_films', blank=True)
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ]
    )
    video_url = models.CharField('Ссылка на видео или файл', max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'






