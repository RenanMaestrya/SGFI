from django.contrib import admin
from .models import Print, User

# Register your models here.
admin.site.register(User)
admin.site.register(Print)