from django.db import models

# Create your models here.
from django.db import models


class Films(models.Model):
    title = models.CharField('Название фильма',max_length=150)
    description = models.CharField('Описание фильма', max_length=350)
    picture = models.ImageField(upload_to='')
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    video_url = models.CharField('Ссылка на видео или файл', max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

