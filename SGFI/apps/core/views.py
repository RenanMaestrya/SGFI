from django.shortcuts import render
from .models import Print
from .forms import PrintForm
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'apps/core/pages/index.html')

class PrintListView(ListView):
    template_name = 'apps/core/pages/dashboard.html'
    model = Print
    context_object_name = 'prints'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['withdrawn_count'] = Print.objects.filter(status='withdrawn').count()
        context['pending_count'] = Print.objects.filter(status='pending').count()
        context['printed_count'] = Print.objects.filter(status='printed').count()
        context['user'] = self.request.user
        return context

class PrintCreateView(CreateView):
    template_name = 'apps/core/pages/form.html'
    model = Print   
    form_class = PrintForm
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['role'] = 'user'
        return context

class HistoryListView(ListView):
    template_name = 'apps/core/pages/history.html'
    model = Print
    context_object_name = 'prints'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['withdrawn_count'] = Print.objects.filter(status='withdrawn').count()
        context['pending_count'] = Print.objects.filter(status='pending').count()
        context['printed_count'] = Print.objects.filter(status='printed').count()
        context['user'] = self.request.user
        return context
    
def LogoutView(request):
    logout(request)
    return redirect('index')