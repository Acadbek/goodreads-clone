# Generated by Django 4.2.4 on 2023-11-22 12:20

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='job',
            field=models.CharField(default=datetime.datetime(2023, 11, 22, 12, 20, 18, 683950, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
