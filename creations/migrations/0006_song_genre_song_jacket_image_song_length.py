# Generated by Django 4.2.6 on 2023-10-17 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0005_release_link_song_bpm_alter_release_release_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='song',
            name='jacket_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='song',
            name='length',
            field=models.DurationField(blank=True, default=datetime.timedelta(0)),
            preserve_default=False,
        ),
    ]