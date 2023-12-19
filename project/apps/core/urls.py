from django.urls import path
from .views import PrintCreateView, PrintListView, IndexView, HistoryListView, LogoutView, PrintUpdateStatusView, WarningCreateView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('solicitar/', PrintCreateView.as_view(), name='solicitar'),
    path('dashboard/', PrintListView.as_view(), name='dashboard'),
    path('historico/', HistoryListView.as_view(), name='historico'),
    path('atualizar_estado/<int:pk>/<str:status>/', PrintUpdateStatusView, name='atualizar_estado'),
    path('aviso/', WarningCreateView.as_view(), name='criar_aviso'),
    path('logout/', LogoutView, name='logout'),
]