# Generated by Django 4.2.1 on 2024-03-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email_verify',
            field=models.BooleanField(default=False),
        ),
    ]
