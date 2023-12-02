import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

def get_file_path(_instance, filename):
    return f"files/{filename}"

# Create your models here.
class User(AbstractUser):
    identification = models.CharField(max_length=255)
    usual_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    preferred_email = models.EmailField(max_length=255)
    google_classroom_email = models.EmailField(max_length=255)
    
    def __str__(self):
        return self.full_name
    
class Print(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('printed', 'Impresso'),
        ('withdrawn', 'Retirado'),
    ]
     
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    attachment = models.FileField(max_length=254, upload_to=get_file_path)
    print_count = models.PositiveIntegerField(default=1)
    withdraw_date = models.DateField()
    withdraw_time = models.TimeField()
    observation = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    withdrawn_at = models.DateTimeField(blank=True, null=True)
    is_sensible = models.BooleanField(default=False)
    
    def __str__(self):
        return self.created_by.username
    
class Warning(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    send_to_all = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.created_at} - {self.title}"