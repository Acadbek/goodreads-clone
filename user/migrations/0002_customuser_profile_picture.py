# Generated by Django 4.2.4 on 2023-11-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pictures'),
        ),
    ]
