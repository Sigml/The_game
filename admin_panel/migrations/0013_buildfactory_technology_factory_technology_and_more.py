# Generated by Django 5.0.7 on 2024-11-25 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0012_alter_age_background_alter_age_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildfactory',
            name='technology',
            field=models.ManyToManyField(blank=True, related_name='required_technology', to='admin_panel.technology'),
        ),
        migrations.AddField(
            model_name='factory',
            name='technology',
            field=models.ManyToManyField(blank=True, related_name='technology', to='admin_panel.technology'),
        ),
        migrations.AddField(
            model_name='factory',
            name='type',
            field=models.CharField(choices=[('MILITARY', 'Wojsko'), ('DEFENSE', 'Obrona'), ('MINING', 'Wydobycie surowców'), ('DEVELOPMENT', 'Rozwój'), ('HOUSING', 'Mieszkalnictwo'), ('WONDERS', 'Cudy świata')], default='MILITARY', max_length=255),
        ),
        migrations.AddField(
            model_name='technology',
            name='prerequisite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_technologies', to='admin_panel.technology'),
        ),
    ]