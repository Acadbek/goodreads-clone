# Generated by Django 4.2.4 on 2023-11-22 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to=''),
        ),
    ]
