from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    identification = models.CharField(max_length=255)
    social_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username