from django import forms
from .models import Print
from django.conf import settings

class PrintForm(forms.ModelForm):
    class Meta:
        model = Print
        fields = ["withdraw_date", "withdraw_time", "print_count", "observation", "attachment"]
        widgets = {
            "withdraw_date": forms.DateInput(attrs={"type": "date", "class": "base__input"}),
            "withdraw_time": forms.TimeInput(attrs={"type": "time", "class": "base__input"}),
            "print_count": forms.NumberInput(attrs={"class": "base__input"}),
            "observation": forms.Textarea(attrs={"class": "base__input textarea", "placeholder": "Adicione informações extras que deseja enviar para o(a) administrador(a) da impressão..." }),
            "attachment": forms.FileInput(attrs={"class": "base__input"}),
        }
