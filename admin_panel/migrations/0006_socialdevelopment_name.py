# Generated by Django 4.2.1 on 2024-06-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0005_remove_socialdevelopment_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialdevelopment',
            name='name',
            field=models.CharField(default='wydarzenie', max_length=100),
        ),
    ]