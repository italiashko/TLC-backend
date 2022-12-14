# Generated by Django 3.2.6 on 2021-09-01 07:45

from django.db import migrations, models
import tlc.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tlc', '0012_alter_productresults_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Без названия', max_length=50, verbose_name='Название')),
                ('file', models.FileField(upload_to='video', validators=[tlc.validators.validate_video_extension])),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
    ]
