# Generated by Django 5.0.7 on 2024-08-07 10:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_panel', '0007_age_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewWorld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_age', to='admin_panel.age')),
                ('alliance', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_alliance', to='admin_panel.alliance')),
                ('army', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_army', to='admin_panel.army')),
                ('build_factory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_build_factories', to='admin_panel.buildfactory')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_country', to='admin_panel.country')),
                ('ecology', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_ecology', to='admin_panel.ecology')),
                ('event', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_event', to='admin_panel.event')),
                ('factory', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_factory', to='admin_panel.factory')),
                ('peace_treaty', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_peace_treaty', to='admin_panel.peacetreaty')),
                ('required_resources', models.ManyToManyField(blank=True, related_name='world_required_resources', to='admin_panel.requiredresources')),
                ('resources', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_resources', to='admin_panel.resources')),
                ('social_development', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_social_development', to='admin_panel.socialdevelopment')),
                ('technology', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_technology', to='admin_panel.technology')),
                ('trade', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_trade', to='admin_panel.trade')),
                ('trade_agreement', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_trade_agreement', to='admin_panel.tradeagreement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_world', to=settings.AUTH_USER_MODEL)),
                ('war', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_war', to='admin_panel.war')),
            ],
        ),
    ]
