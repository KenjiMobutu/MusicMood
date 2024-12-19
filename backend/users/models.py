from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    favorite_genres = models.JSONField(default=list)
    favorite_artists = models.JSONField(default=list)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Changez le `related_name`
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Changez le `related_name`
        blank=True,
    )

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username
