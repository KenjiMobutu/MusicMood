from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    favorite_genres = models.JSONField(default=list)
    favorite_artists = models.JSONField(default=list)
    
    class Meta:
        db_table = 'users'