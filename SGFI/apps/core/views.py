from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'apps/core/pages/index.html')

def form(request):
    return render(request, 'apps/core/pages/form.html')

def dashboard(request):
    role = 'admin'
    return render(request, 'apps/core/pages/dashboard.html', { 'role': role })

def history(request):
    return render(request, 'apps/core/pages/history.html')