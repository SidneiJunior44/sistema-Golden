from django.urls import path
from .views import RequisicoesListView, ReativacaoView, ReativacaoIdIccidCreateView, ReativacaoListView

urlpatterns = [
    path('reativacoes/', ReativacaoListView.as_view(), name='reativacao_list'),
    path('reativacoes/adicionar/', ReativacaoIdIccidCreateView.as_view(), name='reativacao_id_iccid_adicionar'),
    path('reativacao/', ReativacaoView.as_view(), name='reativacao'),
    path('requisicoes/', RequisicoesListView.as_view(), name='requisicoes_list'),
    # Outras URLs...
]