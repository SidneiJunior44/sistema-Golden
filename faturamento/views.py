from django.views.generic import ListView, CreateView
from requisicao.models import Requisicoes, Produto, Clientes
from django.shortcuts import get_object_or_404, redirect
from . import models, forms
from .models import Formulario
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from itertools import chain

class FaturamentoListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = "faturamento_list.html"
    context_object_name = 'requisicoes'
    paginate_by = 10
    permission_required = 'faturamento.view_formulario'  # Substitua 'faturamento' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset()
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim')
        status_faturamento = self.request.GET.get('status_faturamento_filtro')
        cliente = self.request.GET.get('cliente_filtro')
        motivo = self.request.GET.get('motivo_filtro')
        tipo_produto = self.request.GET.get('tipo_produto_filtro')
        contrato_tipo = self.request.GET.get('contrato_tipo_filtro')
        fatura_tipo = self.request.GET.get('fatura_tipo_filtro')
        
        if data_inicio and data_fim:
            queryset = queryset.filter(data__range=[data_inicio, data_fim])
        
        if status_faturamento:
            queryset = queryset.filter(status_faturamento=status_faturamento)
        
        if cliente:
            queryset = queryset.filter(nome=cliente)
        
        if motivo:
            queryset = queryset.filter(motivo=motivo)
        
        if tipo_produto:
            queryset = queryset.filter(tipo_produto=tipo_produto)
        
        if contrato_tipo:
            queryset = queryset.filter(contrato=contrato_tipo)
        
        if fatura_tipo:
            queryset = queryset.filter(tipo_fatura=fatura_tipo)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_faturamento_choices'] = Requisicoes._meta.get_field('status_faturamento').choices
        context['clientes_choices'] = Clientes.objects.all()
        context['motivo_choices'] = Requisicoes._meta.get_field('motivo').choices
        context['tipo_produto_choices'] = Produto.objects.all()
        context['contrato_tipo_choices'] = Requisicoes._meta.get_field('contrato').choices
        context['fatura_tipo_choices'] = Requisicoes._meta.get_field('tipo_fatura').choices
        return context

def update_status_faturamento(request, id):
    if request.method == 'POST':
        requisicao = get_object_or_404(Requisicoes, id=id)
        status_faturamento = request.POST.get('status_faturamento')
        requisicao.status_faturamento = status_faturamento
        requisicao.save()
    return redirect('faturamento_list')

class contratosListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = "contrato_list.html"
    context_object_name = 'contratos_list'
    paginate_by = 10
    permission_required = 'faturamento.view_formulario'  # Substitua 'faturamento' pelo nome do seu aplicativo

class formularioCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Formulario
    template_name = 'Formulario_contratos.html'
    form_class = forms.FormularioForm
    success_url = reverse_lazy('formulario_create')
    permission_required = 'faturamento.add_formulario'  # Substitua 'faturamento' pelo nome do seu aplicativo
