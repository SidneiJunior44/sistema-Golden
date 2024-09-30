from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Rprestador
from .forms import Prestador
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class RprestadorCreateView( PermissionRequiredMixin,LoginRequiredMixin,  CreateView):
    model = Rprestador
    template_name = 'rprestador.html'
    form_class = Prestador
    success_url = reverse_lazy('rprestador')
    permission_required = 'prestadores.add_rprestador'  # Substitua 'prestadores' pelo nome do seu aplicativo

class RprestadorListViews( PermissionRequiredMixin,LoginRequiredMixin,  ListView):
    model = Rprestador
    template_name = "prestador.html"
    context_object_name = 'prestador_list'
    paginate_by = 10
    permission_required = 'prestadores.view_rprestador'  # Substitua 'prestadores' pelo nome do seu aplicativo

class RequisicoesUpdateView( PermissionRequiredMixin,LoginRequiredMixin,  UpdateView):
    model = Rprestador
    template_name = 'rprestador.html'
    form_class = Prestador
    success_url = reverse_lazy('Rprestador')
    permission_required = 'prestadores.change_rprestador'  # Substitua 'prestadores' pelo nome do seu aplicativo
