# Generated by Django 4.2.4 on 2023-11-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='default-user-img.png', upload_to=''),
        ),
    ]