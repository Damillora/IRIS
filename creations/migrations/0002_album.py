# Generated by Django 4.2.6 on 2023-10-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('romanized_title', models.CharField(max_length=255)),
                ('songs', models.ManyToManyField(related_name='songs', to='creations.song')),
            ],
        ),
    ]
