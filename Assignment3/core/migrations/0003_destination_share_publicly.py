# Generated by Django 4.2.11 on 2025-03-05 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_name_destination_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='share_publicly',
            field=models.BooleanField(default=False),
        ),
    ]
