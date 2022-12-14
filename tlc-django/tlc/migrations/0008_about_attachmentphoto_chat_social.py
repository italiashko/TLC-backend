# Generated by Django 3.2.6 on 2021-08-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlc', '0007_alter_article_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Без названия', max_length=50, verbose_name='Название')),
                ('link', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video', verbose_name='Видео')),
                ('text', models.TextField(blank=True, null=True)),
                ('attaches', models.ManyToManyField(to='tlc.AttachmentPhoto')),
            ],
            options={
                'verbose_name': 'О компании',
                'verbose_name_plural': 'О компании',
            },
        ),
    ]
