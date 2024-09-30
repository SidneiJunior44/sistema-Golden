from django.urls import path
from .views import FaturamentoListView, update_status_faturamento, contratosListView, formularioCreateView

urlpatterns = [
    path('', FaturamentoListView.as_view(), name='faturamento_list'),
    path('contrato', contratosListView.as_view(), name='Contrato_list'),
    path('atualizar_status_faturamento/<int:id>/', update_status_faturamento, name='atualizar_status_faturamento'),
    path('formulario/create/', formularioCreateView.as_view(), name='formulario_create'),
]