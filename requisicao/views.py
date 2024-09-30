from typing import Any
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from registrodemanutencao.models import registrodemanutencao
from requisicao.models import Requisicoes
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.conf import settings
from registrodemanutencao.forms import FormulariosUpdateForm
from django.core.mail import send_mail
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
#------------------------------------------------------
class RequisicoesViews(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = "requisicoes.html"
    context_object_name = 'requisicoes'
    paginate_by = 10
    permission_required = "requisicao.view_requisicoes"
    
    def get_queryset(self):
        return Requisicoes.objects.filter(status__in=['Pendente'])
    

  
    
class requisicoescrateview(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = models.Requisicoes
    template_name = 'requisicao_create.html'
    form_class = forms.requisicaoForm
    success_url = reverse_lazy('requisicoes')
    permission_required="requisicao.add_requisicoes"


class RequisicaoDetailView(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    model = models.Requisicoes
    template_name = 'requisicao_detail.html'
    permission_required="requisicao.view_requisicoes"


class RequisicaoUpdateView(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Requisicoes
    form_class = forms.requisicaoForm
    template_name = 'requisicao_update.html'
    context_object_name = 'requisicao'
    success_url = reverse_lazy('requisicao_list')
    permission_required="requisicao.change_requisicoes"

  

class requisicoesdeleteview(PermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = models.Requisicoes
    template_name = 'requisicao_delete.html'
    success_url = reverse_lazy('acompanhamento_requisicao')
    permission_required="requisicao.delete_requisicoes"
#------------------------------------------------------

#------------------------------------------------------
class configuracaodeleteview(PermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = models.Requisicoes
    template_name = 'configuracao_delete.html'
    success_url = reverse_lazy('acompanhamento_requisicao')
    permission_required="requisicao.delete_requisicoes"


class ConfiguracaoListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    template_name = 'configuracao_list.html'
    context_object_name = 'equipamentos'
    permission_required= "requisicao.view_requisicoes"
    
    
    def get_queryset(self):
        requisicoes_queryset = Requisicoes.objects.filter(status__in=['Aprovado pelo CEO'])
        manutencao_queryset = registrodemanutencao.objects.filter(status__in=['Aprovado Inteligência', 'Aprovado pela Diretoria', 'Aprovado pelo CEO'])
        
        # Combine os querysets
        combined_queryset = list(requisicoes_queryset) + list(manutencao_queryset)
        
        return combined_queryset


class ConfiguracaoUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Requisicoes
    form_class = forms.requisicaoForm
    template_name = 'configuracao_update.html'
    context_object_name = 'equipamento'
    success_url = reverse_lazy('ConfiguracaoListView')
    permission_required = "requisicao.change_requisicoes"

class ConfiguracaoUpdateView2(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = registrodemanutencao
    form_class = FormulariosUpdateForm
    template_name = 'configuracao_update.html'
    context_object_name = 'equipamento'
    success_url = reverse_lazy('ConfiguracaoListView')
    permission_required = "requisicao.change_requisicoes"
  

 #------------------------------------------------------   

   
#------------------------------------------------------
class ceoListViews(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = Requisicoes
    template_name = "ceo_list.html"
    context_object_name = 'ceo_list'
    paginate_by = 10
    permission_required="requisicao.view_requisicoes"
    def get_queryset(self):
        return Requisicoes.objects.filter(status__in=['Pendente','Aprovado pela Diretoria'])
  

class ceodetailview(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    model = Requisicoes
    template_name = 'ceo_detail.html'
    permission_required="requisicao.view_requisicoes"


class CeoEntradaDetailView(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    model = registrodemanutencao
    template_name = 'ceo_detalheentrada.html'
    context_object_name = 'manutencoes'
    permission_required="requisicao.view_requisicoes"
#------------------------------------------------------


#------------------------------------------------------


class diretoriaListViews(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    template_name = "diretoria_list.html"
    context_object_name = 'diretoria_list'
    permission_required="requisicao.view_requisicoes"
    
    def get_queryset(self):
        requisicoes_queryset = Requisicoes.objects.filter(status__in=['', ''])
        manutencao_queryset = registrodemanutencao.objects.filter(status='Manutenção')
        
        # Combine os querysets
        combined_queryset = list(requisicoes_queryset) + list(manutencao_queryset)
        
        return combined_queryset
#------------------------------------------------------

#------------------------------------------------------
class expedicaoListViews(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = Requisicoes
    template_name = "expedicao_list.html"
    context_object_name = 'expedicao_list'
    permission_required="requisicao.view_requisicoes"
    
       
    def get_queryset(self):
        requisicoes_queryset = Requisicoes.objects.filter(status__in=['Configurado'])
        manutencao_queryset = registrodemanutencao.objects.filter(status__in=['Configurado'])
        
        # Combine os querysets
        combined_queryset = list(requisicoes_queryset) + list(manutencao_queryset)
        
        return combined_queryset
#------------------------------------------------------
#------------------------------------------------------
class historicoListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = Requisicoes
    template_name = "historico_list.html"
    context_object_name = 'historico_list'
    permission_required="requisicao.view_requisicoes"
    
    def get_queryset(self):
        queryset = Requisicoes.objects.filter(status__in=['Enviado para o Cliente', 'Reprovado pelo CEO'])
        nome = self.request.GET.get('nome')
        id_equipamentos = self.request.GET.get('id_equipamentos')
        
        if nome:
            queryset = queryset.filter(nome__nome__icontains=nome)
        
        if id_equipamentos:
            queryset = queryset.filter(id_equipamentos__icontains=id_equipamentos)
        
        return queryset

#------------------------------------------------------





#------------------------------------------------------
def aprovar_requisicao(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Aprovado pela Diretoria'
    registro.save()
    return redirect('#')

def reprovar_requisicao(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Reprovado pela Diretoria'
    registro.save()
    return redirect('#')
#------------------------------------------------------

#------------------------------------------------------
def reprovar_ceo(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Reprovado pelo CEO'
    registro.save()
    
    return redirect('ceoListViews')


def aprovar_ceo(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Aprovado pelo CEO'
    registro.save()
    subject = f"Manutenção Aprovada: {registro.id}"
    message = f"A manutenção {registro.id} foi aprovada com sucesso. {registro.nome} Status: {registro.status} criar Requisição"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['sjuniorr6@gmail.com']
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    
    

    return redirect('ceoListViews')
    
    
#------------------------------------------------------


#------------------------------------------------------
from django.http import HttpResponse
def configurado_expedicao(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Configurado'
    registro.save()
    return redirect('ConfiguracaoListView')

def expedicao_expedido(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Enviado para o Cliente'
    registro.save()
    return redirect('expedicaoListViews')

def expedicao_expedido2(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Enviado para o Cliente'
    registro.save()
    return redirect('expedicaoListViews')


def expedir_requisicao(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    # Alterar o status do registro para "Configurado"
    registro.status = 'Configurado'
    registro.save()
    return redirect('ConfiguracaoListView')

def expedir_manutencao(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    # Alterar o status do registro para "Configurado"
    registro.status = 'Configurado'
    registro.save()
    return redirect('ConfiguracaoListView')






def configurado_manutencao(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Configurado'
    registro.save()
    return redirect('ConfiguracaoListView')


def expedicao_expedido_manutencao(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Enviado para o Cliente'
    registro.save()
    return redirect('expedicaoListViews')


#------------------------------------------------------
# View para aprovar uma requisição pela diretoria
#------------------------------------------------------
def Reprovar_diretoria(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Reprovado pela Diretoria'
    registro.save()
    
   

# View para reprovar uma requisição pela diretoria
def Aprovar_diretoria(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Aprovado pela Diretoria'  # Corrigido para "Aprovado pela Diretoria"
    registro.save()

    subject = f"Manutenção Aprovada: {registro.id}"
    message = f"A manutenção {registro.id} foi aprovada com sucesso. {registro.nome} Status: {registro.status} criar Requisição"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['sjuniorr6@gmail.com']
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    
    

    return redirect('diretoriaListViews')
#------------------------------------------------------
