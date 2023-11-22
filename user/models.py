from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default="default.jpg")
    job = models.CharField(max_length=100)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    github = models.URLField(blank=True)