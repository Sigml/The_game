# Generated by Django 5.0.7 on 2024-09-18 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_age_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecology',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.country'),
        ),
    ]