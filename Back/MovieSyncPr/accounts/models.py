from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField('Имя пользователя', max_length=60)
    email = models.CharField('Email', max_length=100)
    password = ''
    pass_confirm = ''