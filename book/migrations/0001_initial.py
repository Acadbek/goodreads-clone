# Generated by Django 4.2.4 on 2023-11-21 05:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_tname', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('isbn', models.CharField(max_length=13)),
                ('img', models.ImageField(upload_to='media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('stars_given', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
    ]
