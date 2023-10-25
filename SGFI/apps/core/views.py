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
        {
            'id': 4,
            'requested_at': '19/02/2023',
            'requested_by': 'Maria Silva',
            'attachment': 'Tarefas de Português',
            'attachment_count': 5,
            'withdraw_date': '20/02/2023',
            'withdraw_time': '10:30',
            'status': 'pending',
        },
        {
            'id': 5,
            'requested_at': '20/02/2023',
            'requested_by': 'José Santos',
            'attachment': 'Projetos de Arte',
            'attachment_count': 10,
            'withdraw_date': '21/02/2023',
            'withdraw_time': '15:45',
            'status': 'printed',
        },
        {
            'id': 6,
            'requested_at': '21/02/2023',
            'requested_by': 'Ana Rodrigues',
            'attachment': 'Exercícios de Matemática',
            'attachment_count': 7,
            'withdraw_date': '22/02/2023',
            'withdraw_time': '09:30',
            'status': 'withdrawn',
        },
        {
            'id': 7,
            'requested_at': '22/02/2023',
            'requested_by': 'Ricardo Ferreira',
            'attachment': 'Redações de Português',
            'attachment_count': 9,
            'withdraw_date': '23/02/2023',
            'withdraw_time': '12:15',
            'status': 'pending',
        },
        {
            'id': 8,
            'requested_at': '23/02/2023',
            'requested_by': 'Carla Lima',
            'attachment': 'Exames de Física',
            'attachment_count': 3,
            'withdraw_date': '24/02/2023',
            'withdraw_time': '14:45',
            'status': 'printed',
        },
        {
            'id': 9,
            'requested_at': '24/02/2023',
            'requested_by': 'Manuel Costa',
            'attachment': 'Apresentações de Inglês',
            'attachment_count': 6,
            'withdraw_date': '25/02/2023',
            'withdraw_time': '10:00',
            'status': 'withdrawn',
        },
    ]
    return render(request, 'apps/core/pages/dashboard.html', { 'role': role, 'requests': data })

def history(request):
    role = 'admin'
    data = [
        {
            'id': 1,
            'requested_at': '16/02/2023',
            'requested_by': 'John Doe Foo Bar',
            'withdraw_date': '16/02/2023',
            'content': 'Prova de Matemática, Prova de Química, Prova de Português',
            'withdrawed': 'true'       
        },
        {
            'id': 2,
            'requested_at': '17/02/2023',
            'requested_by': 'Alice Smith',
            'withdraw_date': '18/02/2023',
            'content': 'Prova de Matemática, Prova de Química, Prova de Português',
            'withdrawed': 'true'      
             
        },
        {
            'id': 3,
            'requested_at': '18/02/2023',
            'requested_by': 'Bob Johnson',
            'withdraw_date': '19/02/2023',
            'content': 'Prova de Matemática, Prova de Química, Prova de Português',
            'withdrawed': 'true'
        },
        {
            'id': 4,
            'requested_at': '19/02/2023',
            'requested_by': 'Maria Silva',
            'withdraw_date': '20/02/2023',
            'content': 'Prova de Matemática, Prova de Química, Prova de Português',
            'withdrawed': 'true'       
        },
        {
            'id': 5,
            'requested_at': '20/02/2023',
            'requested_by': 'José Santos',
            'withdraw_date': '21/02/2023',
            'content': 'Prova de Matemática, Prova de Química, Prova de Português',
            'withdrawed': 'false'       
        },
        {
            'id': 6,
            'requested_at': '21/02/2023',
            'requested_by': 'Ana Rodrigues',
            'withdraw_date': '22/02/2023',
            'content': 'Prova de Matemática, Prova de Química, Prova de Português',
            'withdrawed': 'false'
        },
        {
            'id': 7,
            'requested_at': '22/02/2023',
            'requested_by': 'Ricardo Ferreira',
            'withdraw_date': '23/02/2023',
            'content': 'Prova de Matemática, Prova de Química, Prova de Português',
            'withdrawed': 'true'       
        },
        {
            'id': 8,
            'requested_at': '23/02/2023',
            'requested_by': 'Carla Lima',
            'withdraw_date': '24/02/2023',
            'content': 'Prova de Matemática, Prova de Química, Prova de Português',
            'withdrawed': 'false'       
        },
        {
            'id': 9,
            'requested_at': '24/02/2023',
            'requested_by': 'Manuel Costa',
            'withdraw_date': '25/02/2023',
            'content': 'Prova de Matemática, Prova de Química, Prova de Português',
            'withdrawed': 'true'
        }
    ]
       
    return render(request, 'apps/core/pages/history.html', { 'role': role, 'requests': data })