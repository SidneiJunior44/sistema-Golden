from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from . import models, forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import formacompanhamentoForm
from cliente.forms import Cliente
from formacompanhamento.models import Formacompanhamento
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DetailView
from django.http import HttpResponse


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os
from django.conf import settings






class formulariorateview( PermissionRequiredMixin,LoginRequiredMixin,  CreateView):
    model = models.Formacompanhamento
    template_name = 'formacompanhamento.html'
    form_class = forms.formacompanhamentoForm
    context_object_name = 'acomp'
    paginate_by = 10
    success_url = reverse_lazy('formacompanhamento')
    permission_required = 'formacompanhamento.add_Formacompanhamento'  # Substitua 'formacompanhamento' pelo nome do seu aplicativo



class AcompanhamentoListView( PermissionRequiredMixin,LoginRequiredMixin,  ListView):
    model = Formacompanhamento
    template_name = 'facomp.html'
    context_object_name = 'acomp'
    permission_required = 'formacompanhamento.view_Formacompanhamento'  # Substitua 'formacompanhamento' pelo nome do seu aplicativo



class formListView( PermissionRequiredMixin,LoginRequiredMixin,  ListView):
    model = models.Formacompanhamento
    template_name = 'formacompanhamento_detail.html'
    context_object_name = 'acompanhamento'
    permission_required = 'formacompanhamento.view_Formacompanhamento'  # Substitua 'formacompanhamento' pelo nome do seu aplicativo


