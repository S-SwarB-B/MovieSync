# Generated by Django 5.2.1 on 2025-06-03 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_films_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='picture',
            field=models.CharField(max_length=255),
        ),
    ]
