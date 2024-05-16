# Generated by Django 4.2.1 on 2024-05-16 08:56

from django.db import migrations, models
import django.db.models.deletion
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_remove_resources_country_resources_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resources',
            name='country',
        ),
        migrations.AddField(
            model_name='resources',
            name='country',
            field=models.ForeignKey(default=game.models.get_default_country, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='game.country'),
        ),
    ]