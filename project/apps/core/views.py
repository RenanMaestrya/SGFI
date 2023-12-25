from django.core.mail import EmailMessage
from django.utils.html import strip_tags
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Print, User
from .forms import PrintForm, WarningForm
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.mail import send_mail
import boto3
from main.settings import (AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME,
                          AWS_SECRET_ACCESS_KEY, SQS_QUEUE_URL, EMAIL_HOST_USER)
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.mixins import AccessMixin

sqs = boto3.client(
    "sqs",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_S3_REGION_NAME,
)    

def send_warning_email(receiver, title, body):
    send_mail(
        title,
        body,
        recipient_list=[receiver.email],
        from_email=EMAIL_HOST_USER,
    )
    
def send_everyone_warning_email(title, body):
    users = User.objects.all()
    send_mail(
        title,
        body,
        recipient_list=[user.email for user in users],
        from_email=EMAIL_HOST_USER,
    )
    
def send_print_email(receiver, title, body):
    send_mail(
        title,
        body,
        recipient_list=[receiver.email],
        from_email=EMAIL_HOST_USER,
    )

# Create your views here.
class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'apps/core/pages/index.html')

@method_decorator(login_required, name='dispatch') 
class WarningCreateView(CreateView, AccessMixin):
    template_name = 'apps/core/pages/alert-form.html'
    model = Warning
    form_class = WarningForm
    success_url = reverse_lazy('dashboard')
        
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not self.request.user.groups.filter(name="bolsista").exists() and \
        not self.request.user.groups.filter(name="gerente").exists():
            return HttpResponse('Você não tem permissão para acessar esta página.', status=403)
        
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        if form.cleaned_data['send_to_all']:
            message = (
                f"Olá,\n\n"
                f"Veja abaixo a mensagem que foi enviada para todos os usuários do SGFI.\n"
                f"----------------------------------------\n"
                f"{form.cleaned_data['message']}\n"
                f"\n"
                f"Atenciosamente,\n"
                f"Comunicação do Sistema de Gerenciamento da Fila de Impressão\n"
                f"Enviado por: {self.request.user.full_name}\n"
            )
            send_everyone_warning_email(form.cleaned_data['title'], message)
        else:
            message = (
                f"Olá {form.cleaned_data['receiver'].full_name},\n\n"
                f"Veja abaixo a mensagem que lhe foi enviada através do SGFI.\n"
                f"----------------------------------------\n"
                f"{form.cleaned_data['message']}\n"
                f"\n"
                f"Atenciosamente,\n"
                f"Comunicação do Sistema de Gerenciamento da Fila de Impressão\n"
                f"Enviado por: {self.request.user.full_name}\n"
            )
            send_warning_email(form.cleaned_data['receiver'], form.cleaned_data['title'], message)
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class PrintListView(AccessMixin, ListView):
    template_name = 'apps/core/pages/dashboard.html'
    model = Print
    context_object_name = 'prints'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not self.request.user.groups.filter(name="professor").exists() and \
        not self.request.user.groups.filter(name="gerente").exists() and \
        not self.request.user.groups.filter(name="bolsista").exists():
            return HttpResponse('Você não tem permissão para acessar esta página.', status=403)
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        if self.request.user.groups.filter(name="professor").exists():
            context['withdrawn'] = self.get_filtered_prints('printed').order_by('withdraw_date')
            context['withdrawn_count'] = self.get_filtered_prints('printed').count()
        else:
            context['withdrawn'] = self.get_filtered_prints('withdrawn').order_by('withdraw_date')[:10]
            context['withdrawn_count'] = 10
            
        context['pending'] = self.get_filtered_prints('pending').order_by('withdraw_date')
        context['printed'] = self.get_filtered_prints('printed').order_by('withdraw_date')
        context['pending_count'] = self.get_filtered_prints('pending').count()
        context['printed_count'] = self.get_filtered_prints('printed').count()
        context['user'] = self.request.user
        return context

    def get_filtered_prints(self, status):
        if self.request.user.groups.filter(name="professor").exists():
            return self.model.objects.filter(
                created_by=self.request.user,
                status=status
            )
            
        elif self.request.user.groups.filter(name="bolsista").exists():
            return self.model.objects.filter(
                is_sensible=False,
                status=status
            )
        else:
            return self.model.objects.filter(status=status)

    def get_queryset(self):
        return super().get_queryset()
    
@method_decorator(login_required, name='dispatch')
class PrintCreateView(CreateView, AccessMixin):
    template_name = 'apps/core/pages/form.html'
    model = Print   
    form_class = PrintForm
    success_url = reverse_lazy('dashboard')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not self.request.user.groups.filter(name="professor").exists() and \
        not self.request.user.groups.filter(name="bolsista").exists() and \
        not self.request.user.groups.filter(name="gerente").exists():
            return HttpResponse('Você não tem permissão para acessar esta página.', status=403)
        
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        try:
            if form.cleaned_data['withdraw_date'] < datetime.now().date():
                raise ValidationError('Data de retirada não pode ser menor que a data atual')
            
            if form.cleaned_data['withdraw_time'] < datetime.now().time():
                raise ValidationError('Hora de retirada não pode ser menor que a hora atual')
            
        except ValidationError as e:
            messages.error(self.request, str(e))
            return self.form_invalid(form)
        
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class HistoryListView(ListView):
    template_name = 'apps/core/pages/history.html'
    model = Print
    context_object_name = 'prints'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not self.request.user.groups.filter(name="bolsista").exists() and \
        not self.request.user.groups.filter(name="gerente").exists():
            return HttpResponse('Você não tem permissão para acessar esta página.', status=403)
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_filtered_prints(self):            
        if self.request.user.groups.filter(name="bolsista").exists():
            return self.model.objects.filter(
                is_sensible=False
            )
        else:
            return self.model.objects.all()
    
    def get_queryset(self) -> QuerySet[Any]:
        return self.get_filtered_prints().order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

@login_required
def LogoutView(request):
    logout(request)
    return redirect('index')

@login_required
def PrintUpdateStatusView(request, pk, status):
    
    if not request.user.groups.filter(name="bolsista").exists() and \
    not request.user.groups.filter(name="gerente").exists():
        return HttpResponse('Você não tem permissão para acessar esta página.', status=403)
    
    print_request = Print.objects.get(pk=pk)
    print_request.status = status
    if print_request.status == 'withdrawn':
        print_request.withdrawn_at = datetime.now()

    if print_request.status == 'printed':
        attachment_name = print_request.attachment.name.split('/')[-1]
        formatted_date = print_request.created_at.strftime("%d/%m/%Y às %H:%M:%S") 

        subject = 'Impressão Disponível para Retirada'
        recipient_name = print_request.created_by.full_name
        file_description = f"impressão de {attachment_name}"
        print_date = formatted_date

        message = (
            f"Olá {recipient_name},\n\n"
            f"Sua solicitação de {file_description} feita em {print_date} já foi processada e sua impressão está pronta para ser retirada.\n\n"
            f"Detalhes da Impressão:\n"
            f" - Nome do arquivo: {attachment_name}\n"
            f" - Data de solicitação: {print_date}\n"
            f" - Quantidade de cópias: {print_request.print_count}\n"
            f" - Data agendada para retirada: {print_request.withdraw_date.strftime('%d/%m/%Y')}\n"
            f" - Hora agendada para retirada: {print_request.withdraw_time}\n"
            f" - Observações: {strip_tags(print_request.observation) if print_request.observation else 'Nenhuma'}\n"
            f" - Impressão sensível: {'Sim' if print_request.is_sensible else 'Não'}\n"
            f" - Impresso por: {request.user.full_name}\n"
            f"\n"
            f"Por favor, dirija-se à sala de impressão para retirar sua impressão. Em caso de dúvidas, entre em contato conosco.\n\n"
            f"Atenciosamente,\n"
            f"Comunicação do Sistema de Gerenciamento da Fila de Impressão"
        )
        
        send_print_email(print_request.created_by, subject, message)
        
    print_request.save()
    return redirect('dashboard')