from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    def __str__(self) -> str:
        return f"{self.username} ({self.email})"
   