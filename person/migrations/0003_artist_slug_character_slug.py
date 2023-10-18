# Generated by Django 4.2.6 on 2023-10-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_artist_aliases'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='character',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]
