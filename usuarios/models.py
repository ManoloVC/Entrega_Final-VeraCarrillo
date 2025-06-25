from django.contrib.auth.models import AbstractUser
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField()
    edad = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
