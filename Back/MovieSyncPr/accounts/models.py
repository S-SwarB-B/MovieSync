from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    password =  models.CharField(max_length=100)
    picture = models.ImageField(upload_to='pictures/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'