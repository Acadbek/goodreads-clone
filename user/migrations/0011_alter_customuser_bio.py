# Generated by Django 4.2.4 on 2023-11-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_customuser_bio_customuser_github_customuser_job_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(),
        ),
    ]
