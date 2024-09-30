from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class estoqueViews(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = models.estoque
    template_name = "estoque_list.html"
    context_object_name = 'estoque'
    paginate_by = 5
    permission_required = 'estoque.view_estoque'  # Substitua 'estoque' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__nome__icontains=nome)
        return queryset

class estoqueCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = models.estoque
    template_name = 'estoque_create.html'
    form_class = forms.estoqueForm
    success_url = reverse_lazy('estoque_list')
    permission_required = 'estoque.add_estoque'  # Substitua 'estoque' pelo nome do seu aplicativo

class estoqueDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = models.estoque
    template_name = 'estoque_detail.html'
    permission_required = 'estoque.view_estoque'  # Substitua 'estoque' pelo nome do seu aplicativo

class estoqueUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = models.estoque
    template_name = 'estoque_update.html'
    form_class = forms.estoqueForm
    success_url = reverse_lazy('estoque_list')
    permission_required = 'estoque.change_estoque'  # Substitua 'estoque' pelo nome do seu aplicativo

class estoqueDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = models.estoque
    template_name = 'estoque_delete.html'
    success_url = reverse_lazy('estoque_list')
    permission_required = 'estoque.delete_estoque'  # Substitua 'estoque' pelo nome do seu aplicativo

from django.shortcuts import render

@login_required
def acompanhamento_cliente(request):
    return render(request, 'acompanhamento_cliente.html')

@login_required
def acompanhamento_relatorio(request):
    return render(request, 'acompanhamento_relatorio.html')

@login_required
def acompanhamento_requisicao(request):
    return render(request, 'acompanhamento_requisicao.html')

@login_required
def acompanhamento_desempenho(request):
    return render(request, 'acompanhamento_desempenho.html')
