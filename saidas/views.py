from django.shortcuts import render

# Create your views here.
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView ,CreateView,DetailView,UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin



class saidasviews(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = models.saidas
    template_name ="saidas_list.html"
    context_object_name ='saidas_list'
    paginate_by= 5
    permission_required ="saidas.view_saidas"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__nome__icontains=nome)
        return queryset


    
class saidascreateview(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = models.saidas
    template_name = 'saidas_create.html'
    form_class = forms.saidasForm
    success_url = reverse_lazy('saidas_list')
    permission_required ="saidas.add_saidas"
    


class saidasdetailview(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    model = models.saidas
    template_name = 'saidas_detail.html'
    permission_required ="saidas.view_saidas"



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
    return render(request, 'acompanhamento_desmepenho.html')

