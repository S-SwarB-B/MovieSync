# Generated by Django 5.2.1 on 2025-06-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_films_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
