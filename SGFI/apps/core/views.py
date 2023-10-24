from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'apps/core/pages/index.html')

def form(request):
    return render(request, 'apps/core/pages/form.html')

def dashboard(request):
    role = 'admin'
    data = [
        {
            'id': 1,
            'requested_at': '16/02/2023',
            'requested_by': 'John Doe Foo Bar',
            'attachment': 'Provas de Matemática',
            'attachment_count': 16,
            'withdraw_date': '16/02/2023',
            'withdraw_time': '16:30',
            'status': 'pending',
        },
        {
            'id': 2,
            'requested_at': '17/02/2023',
            'requested_by': 'Alice Smith',
            'attachment': 'Provas de História',
            'attachment_count': 8,
            'withdraw_date': '18/02/2023',
            'withdraw_time': '14:15',
            'status': 'printed',
        },
        {
            'id': 3,
            'requested_at': '18/02/2023',
            'requested_by': 'Bob Johnson',
            'attachment': 'Relatórios de Ciências',
            'attachment_count': 12,
            'withdraw_date': '19/02/2023',
            'withdraw_time': '11:45',
            'status': 'withdrawn',
        },
    ]
    return render(request, 'apps/core/pages/dashboard.html', { 'role': role, 'requests': data })

def history(request):
    return render(request, 'apps/core/pages/history.html')