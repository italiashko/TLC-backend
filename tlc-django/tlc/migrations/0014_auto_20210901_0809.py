# Generated by Django 3.2.6 on 2021-09-01 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlc', '0013_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='is_educate',
            field=models.BooleanField(default=False, verbose_name='Документ для раздела Обучение?'),
        ),
        migrations.AddField(
            model_name='video',
            name='is_educate',
            field=models.BooleanField(default=False, verbose_name='Видео для раздела Обучение?'),
        ),
    ]
