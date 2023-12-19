from django import forms
from .models import Print, Warning
from django.conf import settings

class PrintForm(forms.ModelForm):
    class Meta:
        model = Print
        fields = ["withdraw_date", "withdraw_time", "print_count", "observation", "attachment", "is_sensible"]
        widgets = {
            "withdraw_date": forms.DateInput(attrs={"type": "date", "class": "base__input"}),
            "withdraw_time": forms.TimeInput(attrs={"type": "time", "class": "base__input"}),
            "print_count": forms.NumberInput(attrs={"class": "base__input"}),
            "observation": forms.Textarea(attrs={"class": "base__input textarea", "placeholder": "Adicione informações extras que deseja enviar para o(a) administrador(a) da impressão..." }),
            "attachment": forms.FileInput(attrs={"class": "base__input"}),
            "is_sensible": forms.CheckboxInput(attrs={"class": "base__input"}),
        }
        
class WarningForm(forms.ModelForm):
    class Meta:
        model = Warning
        fields = ["title", "message", "receiver", "send_to_all"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "base__input", "name": "title", "placeholder": "Adicione um título para a mensagem"}),
            "message": forms.Textarea(attrs={"class": "base__input textarea", "placeholder": "Adicione informações extras que deseja enviar para o(a) administrador(a) da impressão...", "name": "message" }),
            "receiver": forms.Select(attrs={"class": "base__input", "name": "receiver"}),
            "send_to_all": forms.CheckboxInput(attrs={"class": "base__input", "name": "send_to_all"}),
        }