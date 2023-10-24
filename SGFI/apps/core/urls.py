from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('solicitar/', form, name='solicitar'),
    path('dashboard/', dashboard, name='dashboard'),
    path('historico/', history, name='historico'),
]