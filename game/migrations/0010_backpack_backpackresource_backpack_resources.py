# Generated by Django 5.0.7 on 2024-10-19 16:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0010_factory_quantity_factory_resource'),
        ('game', '0009_remove_newworld_build_factory_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Backpack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backpacks', to='admin_panel.country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backpacks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BackpackResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1000)),
                ('backpack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.backpack')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.resources')),
            ],
        ),
        migrations.AddField(
            model_name='backpack',
            name='resources',
            field=models.ManyToManyField(related_name='backpacks', through='game.BackpackResource', to='admin_panel.resources'),
        ),
    ]
