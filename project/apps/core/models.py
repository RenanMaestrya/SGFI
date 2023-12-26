import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.exceptions import ValidationError
from main.settings import MAX_FILE_SIZE
from django.dispatch import receiver
from django.db.models.signals import post_save



def get_file_path(_instance, filename):
    return f"files/{filename}"

def file_size(value):
    limit = MAX_FILE_SIZE
    if value.size > limit:
        raise ValidationError(f'O tamanho máximo do arquivo é de {limit}MB')

# Create your models here.from django.db.models.signals import post_save

class User(AbstractUser):
    identification = models.CharField(max_length=255)
    usual_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    preferred_email = models.EmailField(max_length=255)
    google_classroom_email = models.EmailField(max_length=255)
            
    def assign_group(self):
        group_name = None
        
        if self.role == 'Professor':
            group_name = 'professor'
        elif self.role == 'Aluno':
            group_name = 'aluno'
        
        if group_name:
            try:
                group = Group.objects.get(name=group_name)
                self.groups.add(group)
            except Group.DoesNotExist:
                print(f'Group {group_name} does not exist')

    def __str__(self):
        return self.full_name


@receiver(post_save, sender=User)
def user_post_save(sender, instance, **kwargs):
    if not kwargs['created']:
        instance.assign_group()

    
class Print(models.Model):  
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('printed', 'Impresso'),
        ('withdrawn', 'Retirado'),
    ]
     
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    attachment = models.FileField(max_length=254, upload_to=get_file_path, validators=[file_size])
    print_count = models.PositiveIntegerField(default=1)
    withdraw_date = models.DateField()
    withdraw_time = models.TimeField()
    observation = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    withdrawn_at = models.DateTimeField(blank=True, null=True)
    is_sensible = models.BooleanField(default=False)
    
    def __str__(self):
        return self.created_by.username
    
    def get_status_display(self):
        status_mapping = dict(self.STATUS_CHOICES)
        return status_mapping.get(self.status, self.status)
    
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