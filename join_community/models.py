# join_community/models.py
from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=255, unique=True, null=True)
    email = models.EmailField(unique=True, null=True)
    subscription = models.BooleanField(default=False, null=True)
    password = models.CharField(max_length=50, null=True)
   
    def __str__(self):
        return self.username
