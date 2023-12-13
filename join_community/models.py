# join_community/models.py
from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    subscription = models.BooleanField(default=False)

    def __str__(self):
        return self.username
