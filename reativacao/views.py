import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ReativacaoForm, IdIccidFormSet, IdIccidForm
from .models import Reativacao, IdIccid, Clientes
from django.views.generic import ListView
from requisicao.models import Requisicoes
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class ReativacaoIdIccidCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'reativacao.add_reativacao'  # Substitua 'reativacao' pelo nome do seu aplicativo

    def get(self, request):
        reativacao_form = ReativacaoForm()
        id_iccid_formset = IdIccidFormSet(queryset=IdIccid.objects.none())
        return render(request, 'reativacao_id_iccid_form.html', {
            'reativacao_form': reativacao_form,
            'id_iccid_formset': id_iccid_formset
        })

    def post(self, request):
        reativacao_form = ReativacaoForm(request.POST)
        id_iccid_formset = IdIccidFormSet(request.POST)
        
        if reativacao_form.is_valid() and id_iccid_formset.is_valid():
            reativacao = reativacao_form.save()
            
            # Processar campos adicionados dinamicamente
            for key, value in request.POST.items():
                if key.startswith('id_idiccid_set-') and key.endswith('-ccid_equipamentos'):
                    contador = key.split('-')[1]
                    ccid_equipamentos = value
                    
                    if ccid_equipamentos:
                        IdIccid.objects.create(
                            reativacao=reativacao,
                            ccid_equipamentos=ccid_equipamentos
                        )
                        
                        # Fazer a reativação usando a API da 1nce
                        token = self.obter_token_acesso()
                        if token:
                            self.reativar_equipamento(ccid_equipamentos, token)
            
            return redirect('reativacao_id_iccid_adicionar')
        
        return render(request, 'reativacao_id_iccid_form.html', {
            'reativacao_form': reativacao_form,
            'id_iccid_formset': id_iccid_formset
        })

    def obter_token_acesso(self):
        url = "https://api.1nce.com/management-api/v1/oauth/token"
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        data = {
            "grant_type": "password",
            "username": "seu_usuario",
            "password": "sua_senha"
        }
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            token = response.json().get("access_token")
            print("Token de acesso obtido com sucesso!")
            return token
        else:
            print(f"Erro ao obter token de acesso: {response.status_code}")
            print(response.text)
            return None

    def reativar_equipamento(self, ccid_equipamentos, token):
        url = "https://api.1nce.com/management-api/v1/sims"
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        data = [
            {
                "imei_lock": False,
                "status": "Enabled",
                "ccid_equipamentos": ccid_equipamentos
            }
        ]
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            print("Equipamento reativado com sucesso!")
        else:
            print(f"Erro ao reativar equipamento: {response.status_code}")
            print(response.text)

class RequisicoesListView( PermissionRequiredMixin,LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = 'requisicoes_list.html'
    context_object_name = 'requisicoes'
    paginate_by = 10
    permission_required = 'reativacao.view_reativacao'  # Substitua 'reativacao' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')
        status = self.request.GET.get('status')

        if nome:
            queryset = queryset.filter(nome__nome__icontains=nome)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

class ReativacaoListView( PermissionRequiredMixin,LoginRequiredMixin, View):
    permission_required = 'reativacao.view_reativacao'  # Substitua 'reativacao' pelo nome do seu aplicativo

    def get(self, request):
        cliente_filtro = request.GET.get('cliente_filtro')
        status_reativacao_filtro = request.GET.get('status_reativacao_filtro')

        reativacoes = Reativacao.objects.all()

        if cliente_filtro:
            reativacoes = reativacoes.filter(nome__id=cliente_filtro)
        if status_reativacao_filtro:
            reativacoes = reativacoes.filter(status_reativacao=status_reativacao_filtro)

        return render(request, 'reativacao_list.html', {
            'reativacoes': reativacoes,
            'clientes_choices': Clientes.objects.all(),
            'status_reativacao_choices': Reativacao.STATUS_CHOICES,
        })

    def post(self, request):
        id_iccid = get_object_or_404(IdIccid, pk=request.POST.get('id_iccid'))
        form = IdIccidForm(request.POST, instance=id_iccid)
        if form.is_valid():
            form.save()
            return redirect('reativacao_list')
        return render(request, 'reativacao_list.html', {
            'reativacoes': Reativacao.objects.all(),
            'clientes_choices': Clientes.objects.all(),
            'status_reativacao_choices': Reativacao.STATUS_CHOICES,
            'form': form,
        })

@method_decorator(login_required, name='dispatch')
class ReativacaoView( PermissionRequiredMixin,LoginRequiredMixin, View):
    permission_required = 'reativacao.view_reativacao'  # Substitua 'reativacao' pelo nome do seu aplicativo

    def get(self, request):
        return render(request, 'reativacao.html')
