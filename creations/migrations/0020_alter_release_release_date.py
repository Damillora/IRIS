# Generated by Django 4.2.6 on 2023-10-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0019_release_illustrator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]