# Generated by Django 5.0.7 on 2024-09-09 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_age_image'),
        ('game', '0002_remove_newworld_resources_alter_newworld_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='newworld',
            name='resources',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_resources', to='admin_panel.resources'),
        ),
        migrations.AlterField(
            model_name='newworld',
            name='age',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_age', to='admin_panel.age'),
        ),
    ]
