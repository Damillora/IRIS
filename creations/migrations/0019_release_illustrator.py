# Generated by Django 4.2.6 on 2023-10-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_artist_slug_character_slug'),
        ('creations', '0018_song_original_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='illustrator',
            field=models.ManyToManyField(blank=True, related_name='illustrators', to='person.artist'),
        ),
    ]
