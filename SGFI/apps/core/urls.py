from django.urls import path
from .views import PrintCreateView, PrintListView, IndexView, HistoryListView, LogoutView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('solicitar/', PrintCreateView.as_view(), name='solicitar'),
    path('dashboard/', PrintListView.as_view(), name='dashboard'),
    path('historico/', HistoryListView.as_view(), name='historico'),
    path('logout/', LogoutView, name='logout'),
]