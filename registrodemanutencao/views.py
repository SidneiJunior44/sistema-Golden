

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import os
from django.conf import settings
from .models import registrodemanutencao
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from django.core.mail import send_mail
from django.contrib.auth.mixins import  PermissionRequiredMixin,LoginRequiredMixin 
# Importações dos modelos e formulários
from .models import registrodemanutencao, ImagemRegistro,retorno
from requisicao.models import Requisicoes
from .forms import FormulariosForm, FormulariosUpdateForm,ImagemRegistroFormSet, registrodemanutencao
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from.forms import RetornoForm
# View para listar todos os registros de manutenção com paginação.4
#-----------------------------------------------------------------------

class entradasListView( PermissionRequiredMixin,LoginRequiredMixin , ListView):
    model = registrodemanutencao
    template_name = "registro_das_entradas.html"
    context_object_name = 'dasentradas'
    paginate_by = 6
    permission_required = 'registrodemanutencao.view_registrodemanutencao'  # Substitua 'registrodemanutencao' pelo nome do seu aplicativo
    
    def get_queryset(self):
        queryset = registrodemanutencao.objects.filter(status__in=['Pendente'])
        return queryset
#----------------------------------------------------------------------------

class FormularioListView( PermissionRequiredMixin,LoginRequiredMixin , ListView):
    model = registrodemanutencao
    template_name = "registrodemanutencaolist.html"
    context_object_name = 'registrodemanutencao'
    paginate_by = 6
    permission_required = 'registrodemanutencao.view_registrodemanutencao'  # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome', '')
        status = self.request.GET.get('status', '')
        
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if status:
            queryset = queryset.filter(status=status)
       
        return queryset

#------------------------------------------------------------------------------
class FormulariosCreateView( PermissionRequiredMixin,LoginRequiredMixin , CreateView):
    model = registrodemanutencao
    form_class = FormulariosForm
    template_name = 'registrodemanutencao_create.html'
    success_url = reverse_lazy('FormulariosCreateView')
    permission_required = 'registrodemanutencao.add_registrodemanutencao'  # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

#----------------------------------------------------------------------------------



# View para atualizar um registro de manutenção existente.
class FormulariosUpdateView(LoginRequiredMixin,  UpdateView):
    model = registrodemanutencao
    form_class = FormulariosUpdateForm
    template_name = 'registrodemanutencao_update.html'
    success_url = reverse_lazy('entradasListView')
     # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, request.FILES, instance=self.object)
        imagens_formset = ImagemRegistroFormSet(request.POST, request.FILES, instance=self.object)

        if form.is_valid() and imagens_formset.is_valid():
            return self.form_valid(form, imagens_formset)
        else:
            return self.form_invalid(form, imagens_formset)

    def form_valid(self, form, imagens_formset):
        self.object = form.save()
        imagens_formset.instance = self.object
        imagens_formset.save()
        return redirect(self.success_url)

    def form_invalid(self, form, imagens_formset):
        return render(self.request, self.template_name, {
            'form': form,
            'imagens_formset': imagens_formset
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['imagens_formset'] = ImagemRegistroFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['imagens_formset'] = ImagemRegistroFormSet(instance=self.object)
        return context
    
    

class FormularioDetailView(LoginRequiredMixin,  DetailView):
    model = registrodemanutencao
    template_name = 'registrodemanutencao_detail.html'
    context_object_name = 'registrodemanutencao_detail'
     # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

# View para deletar um registro de manutenção.
#-------------------------------------------------------------------------

def aprovar_manut(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Aprovado Inteligência'
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
    
    return redirect('entradasListView')

def reprovar_manut(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Manutenção'
    registro.save()
    return redirect('entradasListView')

# View para listar registros de manutenção filtrados pelo status 'Aprovado', 'Reprovado' ou 'Pendente'.

#--------------------------------------

class ConfiguracaoListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = 'configuracao_list.html'
    context_object_name = 'registros'
    paginate_by = 6
    success_url = reverse_lazy('configuracao_list')
    permission_required = 'registrodemanutencao.view_registrodemanutencao' 
     # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = registrodemanutencao()
        return context
#--------------------------------------

class expedicaoListView( PermissionRequiredMixin,LoginRequiredMixin , ListView):
    model = Requisicoes
    template_name = 'expedicao_list.html'  # Nome do seu template para status "configuração"
    context_object_name = 'requisicoes'
    permission_required = 'registrodemanutencao.view_registrodemanutencao'  # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            Q(status__iexact='Expedido') | Q(status__iexact='Aprovado')
        )
        print(queryset.query)  # Isso imprimirá a consulta SQL no console
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione os registros de manutenção ao contexto
        context['registros_manutencao'] = registrodemanutencao.objects.filter(
            Q(status__iexact='Expedido') | Q(status__iexact='Aprovado')
        )
        return context

#-----------------------------------------------------------------------------------

# View para exibir os detalhes de uma expedição específica.
class expedicaoDetailView( PermissionRequiredMixin,LoginRequiredMixin , DetailView):
    model = ImagemRegistro
    template_name = 'expedicao_detail.html'
    context_object_name = 'expedicoes'
    permission_required = 'registrodemanutencao.view_registrodemanutencao'  # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

# View para exibir os detalhes de uma configuração específica.
class configDetailView(LoginRequiredMixin, DetailView):
    model = registrodemanutencao
    template_name = 'config_detail.html'
    context_object_name = 'config_detail'
      # Substitua 'registrodemanutencao' pelo nome do seu aplicativo



from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from django.http import HttpResponse
import os
from django.conf import settings

def download_pdf(request, pk):
    try:
        registro = registrodemanutencao.objects.get(pk=pk)
    except registrodemanutencao.DoesNotExist:
        return HttpResponse("Registro não encontrado.", status=404)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="registro-manutencao-{pk}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.setTitle(f'Registro de Manutenção - {pk}')

    # Defina as fontes e cores
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.HexColor("#004B87"))

    # Cabeçalho
    y_position = 750
    p.drawString(100, y_position, "Relatório de Manutenção")
    y_position -= 30

    # Adicionar as imagens lado a lado com fundo branco
    imagem_padrao = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/SIDNEISIDNEISIDNEI.png')
    imagem_qrcode = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/qrcode.png')
    image_width = 200
    image_height = 100
    page_width, page_height = letter
    total_width = image_width * 2 + 20  # Largura total das duas imagens com um espaço entre elas
    x_position = (page_width - total_width) / 2

    # Desenhar um retângulo branco como fundo para as imagens
    p.setFillColor(colors.white)
    p.rect(x_position - 10, y_position - image_height - 10, total_width + 20, image_height + 20, fill=1)

    # Desenhar a primeira imagem
    p.drawImage(imagem_padrao, x_position, y_position - image_height, width=image_width, height=image_height)
    # Desenhar a segunda imagem ao lado da primeira
    p.drawImage(imagem_qrcode, x_position + image_width + 20, y_position - image_height, width=image_width, height=image_height)
    y_position -= (image_height + 20)

    # Restaurar a fonte para o conteúdo principal
    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    # Função para desenhar texto formatado
    def draw_text(p, text, x, y, max_width):
        lines = text.split('\n')
        for line in lines:
            if p.stringWidth(line, "Helvetica", 12) > max_width:
                words = line.split(' ')
                current_line = ""
                for word in words:
                    if p.stringWidth(current_line + word, "Helvetica", 12) < max_width:
                        current_line += word + " "
                    else:
                        p.drawString(x, y, current_line)
                        y -= 20
                        current_line = word + " "
                p.drawString(x, y, current_line)
                y -= 20
            else:
                p.drawString(x, y, line)
                y -= 20
        return y

    # Função para verificar se há espaço suficiente na página atual
    def check_space(p, y_position, required_space):
        if y_position - required_space < 50:
            p.showPage()
            p.setFont("Helvetica", 12)
            p.setFillColor(colors.black)
            return 750
        return y_position

    # Desenhe o conteúdo do PDF
    y_position = draw_text(p, f"Nome: {registro.nome}", 100, y_position, 400)
    y_position = draw_text(p, f"Tipo de Entrada: {registro.tipo_entrada}", 100, y_position, 400)
    y_position = draw_text(p, f"Tipo de Produto: {registro.tipo_produto}", 100, y_position, 400)
    y_position = draw_text(p, f"Motivo: {registro.motivo}", 100, y_position, 400)
    y_position = draw_text(p, f"Tipo Customização: {registro.tipo_customizacao}", 100, y_position, 400)
    y_position = draw_text(p, f"Entregue por/Retirado por: {registro.entregue_por_retirado_por}", 100, y_position, 400)
    y_position = draw_text(p, f"Recebimento: {registro.recebimento}", 100, y_position, 400)
    y_position = draw_text(p, f"Manutenção Equipamentos: {registro.manutencaoequipamentos}", 100, y_position, 400)
    y_position = draw_text(p, f"Retorno Equipamentos: {registro.retornoequipamentos}", 100, y_position, 400)
    y_position = draw_text(p, f"Faturamento: {registro.faturamento}", 100, y_position, 400)
    y_position = draw_text(p, f"Setor: {registro.setor}", 100, y_position, 400)
    y_position = draw_text(p, f"Customização: {registro.customizacao}", 100, y_position, 400)
    y_position = draw_text(p, f"Número Equipamento: {registro.numero_equipamento}", 100, y_position, 400)
    y_position = draw_text(p, f"Tratativa: {registro.tratativa}", 100, y_position, 400)
    y_position = draw_text(p, f"Status: {registro.status}", 100, y_position, 400)

    # Iterar sobre todas as imagens relacionadas e desenhá-las no PDF
    
    for imagem in registro.imagens.all():
        if imagem.imagem:  # Verifique se a imagem existe
            # Desenhe o ID da imagem, o setor e o tipo de problema
            y_position = draw_text(p, f"ID: {imagem.id} - Descrição: {imagem.descricao} - Tipo Problema: {imagem.tipo_problema}", 100, y_position, 400)

            # Adicionar lógica para escrever texto explicativo no campo "tratativa"
            if imagem.tipo_problema == "Oxidação":
                texto_tratativa = """
            Sobre a Manutenção Realizada:
            Para resolver o problema do equipamento,
            foram realizadas as tratativas necessárias e alguns testes posteriores, porém,
            sem sucesso, sendo assim será necessária a troca do dispositivo.
            Atenciosamente,
            Laboratório Técnico. 
        """
            elif imagem.tipo_problema == "Placa Danificada":
                texto_tratativa = """
            Sobre a Manutenção Realizada:
            Para resolver o problema do equipamento,
            foram realizadas as tratativas necessárias e alguns testes
            posteriores, porém, sem sucesso, 
            sendo assim será necessária a troca do dispositivo.
            Atenciosamente,
            Laboratório Técnico
        """
            elif imagem.tipo_problema == "Placa danificada SEM CUSTO":
                texto_tratativa = """A placa do equipamento está danificada, 
                mas a reparação será realizada sem custo."""
            elif imagem.tipo_problema == "USB Danificado":
                texto_tratativa ="""
            Sobre a Manutenção Realizada:
            Para resolver o problema do equipamento, 
            foram realizadas as tratativas necessárias e alguns testes posteriores,
              porém, sem sucesso, sendo assim será necessária a troca do dispositivo.
            Atenciosamente,
            Laboratório Técnico.
        """
            elif imagem.tipo_problema == "USB Danificado SEM CUSTO":
                texto_tratativa = """A porta USB do equipamento está danificada,
                  mas a reparação será realizada sem custo."""
            elif imagem.tipo_problema == "Botão de acionamento Danificado":
                texto_tratativa = """O botão de acionamento do equipamento está danificado, 
                dificultando seu uso."""
            elif imagem.tipo_problema == "Botão de acionamento Danificado SEM CUSTO":
                texto_tratativa = """O botão de acionamento do equipamento está danificado,
                  mas a reparação será realizada sem custo."""
            elif imagem.tipo_problema == "Antena LoRa Danificada":
                texto_tratativa = """
            Sobre a Manutenção Realizada:
            Diante deste diagnóstico e após as tratativas, 
            afirmamos que será necessário a troca do dispositivo.
            Atenciosamente,
            Laboratório Técnico
        """
            elif imagem.tipo_problema == "Sem problemas Identificados":
                texto_tratativa = """
            Sobre a Manutenção Realizada:
            Gostaríamos de informar que concluímos com sucesso as manutenções necessárias no equipamento
              que nos foi confiado para reparo. Após uma análise cuidadosa,
                identificamos e corrigimos os problemas que estavam impactando o seu funcionamento adequado.
            Atenciosamente,
            Laboratório Técnico. 
        """
            else:
                texto_tratativa = "Descrição genérica para problemas não especificados."

            y_position = draw_text(p, f"Tratativa: {texto_tratativa}", 100, y_position, 400)

            # Desenhe a imagem
            caminho_imagem = os.path.join(settings.MEDIA_ROOT, str(imagem.imagem))
            if y_position - 100 < 50:  # Verifique se há espaço suficiente para a imagem na página atual
                p.showPage()  # Crie uma nova página se necessário
                y_position = 750  # Redefina a posição Y para o topo da nova página
            p.drawImage(caminho_imagem, 100, y_position - 100, width=200, height=100)
            y_position -= 120

    # Feche o objeto PDF e entregue o PDF ao navegador.
    p.showPage()
    p.save()
    return response



class CriarRetornoView(CreateView):
    model = retorno
    form_class = RetornoForm
    template_name = 'criar_retorno.html'
    

    def form_valid(self, form):
        self.object = form.save()
        return redirect('download_pdf', pk=self.object.pk)

class DownloadPDFView(DetailView):
    model = retorno

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="registro-manutencao-{self.object.pk}.pdf"'

        p = canvas.Canvas(response, pagesize=letter)
        p.setTitle(f'Registro de Manutenção - {self.object.pk}')

        # Defina as fontes e cores
        p.setFont("Helvetica-Bold", 16)
        p.setFillColor(colors.HexColor("#004B87"))

        # Cabeçalho
        y_position = 750
        p.drawString(100, y_position, "Relatório de Manutenção")
        y_position -= 30

        # Adicionar as imagens lado a lado com fundo branco
        imagem_padrao = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/SIDNEISIDNEISIDNEI.png')
        imagem_qrcode = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/qrcode.png')
        image_width = 200
        image_height = 100
        page_width, page_height = letter
        total_width = image_width * 2 + 20  # Largura total das duas imagens com um espaço entre elas
        x_position = (page_width - total_width) / 2

        # Desenhar um retângulo branco como fundo para as imagens
        p.setFillColor(colors.white)
        p.rect(x_position - 10, y_position - image_height - 10, total_width + 20, image_height + 20, fill=1)

        # Desenhar a primeira imagem
        p.drawImage(imagem_padrao, x_position, y_position - image_height, width=image_width, height=image_height)
        # Desenhar a segunda imagem ao lado da primeira
        p.drawImage(imagem_qrcode, x_position + image_width + 20, y_position - image_height, width=image_width, height=image_height)
        y_position -= (image_height + 20)

        # Adicionar a imagem do campo 'imagem' do modelo 'retorno'
        if self.object.imagem:
            image_path = os.path.join(settings.MEDIA_ROOT, str(self.object.imagem))
            p.drawImage(image_path, 100, y_position - 200, width=200, height=200)
            y_position -= 220

        # Restaurar a fonte para o conteúdo principal
        p.setFont("Helvetica", 12)
        p.setFillColor(colors.black)

        #   # Desenhe o conteúdo do PDF
        p.drawString(100, y_position, f"Cliente: {self.object.cliente}")
        y_position -= 20
        p.drawString(100, y_position, f"Produto: {self.object.produto}")
        y_position -= 20
        p.drawString(100, y_position, f"Tipo de Problema: {self.object.tipo_problema}")
        y_position -= 20
        p.drawString(100, y_position, f"ID Equipamentos: {self.object.id_equipamentos}")
        y_position -= 20
       

        # Feche o objeto PDF e entregue o PDF ao navegador.
        p.showPage()
        p.save()
        return response


class ListaRetornosView(ListView):
    model = retorno
    template_name = 'lista_retornos.html'
    context_object_name = 'retornos'





def minha_view(request):
    if request.method == 'POST':
        form = FormulariosUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('alguma_url_de_sucesso')
    else:
        form = FormulariosUpdateForm()
    return render(request, 'meu_template.html', {'form': form})
# Função para aprovar um registro de manutenção.


class historico_manutencaoListView( PermissionRequiredMixin,LoginRequiredMixin , ListView):
    model = registrodemanutencao
    template_name = 'historico_manutencao.html'  # Nome do seu template para status "configuração"
    context_object_name = 'dasentradas'
    permission_required = 'registrodemanutencao.view_registrodemanutencao'  # Substitua 'registrodemanutencao' pelo nome do seu aplicativo
    
    def get_queryset(self):
        queryset = registrodemanutencao.objects.filter(status__in=['Aprovado Inteligência', 'Reprovado Inteligência','Reprovado pela Diretoria','Aprovado pela Diretoria','Enviado para o Cliente'])
        nome = self.request.GET.get('nome')
        retornoequipamentos = self.request.GET.get('retornoequipamentos')
        
        if nome:
            queryset = queryset.filter(nome__nome__icontains=nome)
        
        if retornoequipamentos:
            queryset = queryset.filter(retornoequipamentos__icontains=retornoequipamentos)
        
        return queryset

@login_required
def aprovar_manutencao(request, id):  # Alterar o nome da função para corresponder ao URL
    requisicao = get_object_or_404(registrodemanutencao, id=id)
    requisicao.status = 'Aprovado Inteligência'  # Certifique-se de que este é o status correto
    requisicao.save()
    return redirect('entradasListView')

@login_required
def reprovar_manutencao(request, id):  # Alterar o nome da função para corresponder ao URL
    requisicao = get_object_or_404(registrodemanutencao, id=id)
    requisicao.status = 'Manutenção'  # Certifique-se de que este é o status correto
    requisicao.save()
    return redirect('entradasListView')

# Função decorada com @login_required para garantir que apenas usuários autenticados possam acessá-la.
@login_required
def rejeitadas(request, id):
    manutencao = get_object_or_404(registrodemanutencao, id=id)
    manutencao.status = 'Aprovado'
    manutencao.save()
    return redirect('rejeitadas')

# Função para renderizar o formulário de manutenção.
@login_required
def formulariom_view(request):
    return render(request, 'registrodemanutencao.html')

# Função para listar registros de manutenção.
@login_required
def manutencaolist(request):
    return render(request, 'manutencao_list.html')
