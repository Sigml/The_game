# Generated by Django 5.0.7 on 2024-09-09 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_newworld_resources'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newworld',
            name='resources',
        ),
    ]
