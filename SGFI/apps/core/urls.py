from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('form/', form, name='form'),
    path('dashboard/', dashboard, name='dashboard'),
    path('history/', history, name='history'),
]