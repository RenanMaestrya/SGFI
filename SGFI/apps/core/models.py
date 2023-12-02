from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    identification = models.CharField(max_length=255)
    social_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username
    
class Print(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('printed', 'Impresso'),
        ('withdrawn', 'Retirado'),
    ]
     
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    attachment = models.FileField(max_length=254, upload_to='uploads/')
    print_count = models.PositiveIntegerField(default=1)
    withdraw_date = models.DateField()
    withdraw_time = models.TimeField()
    observation = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    withdrawn_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.created_by.username