# Generated by Django 5.0.7 on 2024-11-29 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0014_remove_resources_country_remove_resources_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryresource',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources_country', to='admin_panel.resources'),
        ),
    ]
