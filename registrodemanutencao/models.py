from django.db import models

# Create your models here.
from django.db import models
from acompanhamento.models import Clientes   
from produto.models import Produto    

class registrodemanutencao(models.Model):
    TRATATIVAS = [
        ('Oxidação', 'Oxidação'),
        ('Placa Danificada', 'Placa Danificada'),
        ('USB Danificado', 'USB Danificado'),
        ('Botão de acionamento Danificado', 'Botão de acionamento Danificado'),
        ('Antena LoRa Danificada', 'Antena LoRa Danificada'),
        ('USB Sem problemas Identificados', 'USB Sem problemas Identificados'),
    ]

   

    TIPO_ENVIO = [
        ('Agente', 'Agente'),
        ('Retirada', 'Retirada'),
        ('Motoboy', 'Motoboy'),
        ('Transportadora', 'Transportadora'),
        ('Correio', 'Correio'),
        ('Comercial', 'Comercial'),
    ]

    MOTIVOS = [
        ('', ''),
        ('Manutenção', 'Manutenção'),
        ('Devolução/Estoque', 'Devolução/Estoque'),
    ]

    FATURAMENTO = [
        ('', ''),
        ('Com_Custo', 'Com Custo'),
        ('Sem_Custo', 'Sem Custo'),
    ]

    STATUS_CHOICES = [
        ('Aprovado', 'Aprovado'),
        ('Reprovado pela Diretoria', 'Reprovado pela Diretoria'),
        ('Aprovado pela Diretoria', 'Aprovado pela Diretoria'),
        ('Pendente', 'Pendente'),
        ('Expedição', 'Expedição'),
        ('expedido', 'expedido'),
    ]

    ENTRADA = [
        ('Manutenção', 'Manutenção'),
        ('Devolução/Estoque', 'Devolução/Estoque'),
    ]
    SETOR = [
        ('Entrada', 'Entrada'),
        ('Manutenção', 'Manutenção'),
        ('configuração', 'configuração'),
    ]
   

    CUSTOMIZACOES = [
        ('', ''),
        ('Sem customização', 'Sem customização'),
        ('Caixa de papelão', 'Caixa de papelão'),
        ('Caixa de papelão (bateria desacoplada)', 'Caixa de papelão (bateria desacoplada)'),
        # Adicione o restante dos valores conforme necessário
    ]

    RECEBIMENTO_TIPO = [
        ('Correios/Transportadora', 'Correios/Transportadora'),
        ('Entrega na base', 'Entrega na base'),
        ('Retirado pelo cliente', 'Retirado pelo cliente'),
    ]

    nome = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='formulario_nome')
    tipo_entrada = models.CharField(choices=ENTRADA, null=True, blank=True, max_length=50)
    tipo_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='formulario_produto')
    motivo = models.CharField(choices=MOTIVOS, null=True, blank=True, max_length=50)
    tipo_customizacao = models.CharField(choices=CUSTOMIZACOES, null=True, blank=True, max_length=50)
    recebimento = models.CharField(choices=RECEBIMENTO_TIPO, null=True, blank=True, max_length=50)
    entregue_por_retirado_por = models.CharField(max_length=100, default="")
    id_equipamentos = models.CharField(max_length=100, blank=True, default='')
    manutencaoequipamentos= models.TextField(max_length=250, blank=True, default='')
    retornoequipamentos= models.TextField(max_length=250, blank=True, default='')
    faturamento = models.CharField(choices=FATURAMENTO, null=True, blank=True, max_length=50)
    
    setor = models.CharField(choices=SETOR, null=True, blank=True, max_length=50)
    customizacao = models.TextField(max_length=250, blank=True, default='')
    numero_equipamento = models.TextField(max_length=250, blank=True, default='')
    tratativa = models.CharField(choices=TRATATIVAS, null=True, blank=True, max_length=50)
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)
    status = models.CharField( default='Pendente', max_length=50, null=True, blank=True)
   
   



class ImagemRegistro(models.Model):

    SETORID = [
        ('Retorno', 'Retorno'),
        ('expedicao', 'expedicao'),
        ('Manutenção', 'Manutenção'),
        ('configurção', 'configuração'),
       
    ]
    TIPO_PROBLEMAS = [
        ('Oxidação', 'Oxidação'),
        ('Placa Danificada', 'Placa Danificada'),
        ('Placa danificada SEM CUSTO', 'Placa danificada SEM CUSTO'),
        ('USB Danificado', 'USB Danificado'),
        ('USB Danificado SEM CUSTO', 'USB Danificado SEM CUSTO'),
        ('Botão de acionamento Danificado', 'Botão de acionamento Danificado'),
        ('Botão de acionamento Danificado SEM CUSTO', 'Botão de acionamento Danificado SEM CUSTO'),
        ('Antena LoRa Danificada', 'Antena LoRa Danificada'),
        ('Sem problemas Identificados', 'Sem problemas Identificados'),
    ]
    tipo_problema = models.CharField(choices=TIPO_PROBLEMAS, null=True, blank=True, max_length=50)
    registro = models.ForeignKey(registrodemanutencao, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='imagens_registros/')
    descricao = models.CharField(max_length=255, blank=True)
    setorid = models.CharField(choices=SETORID, default='', max_length=50, null=True, blank=True)
    def __str__(self):
        
        descricao_display = f": {self.descricao}" if self.descricao else ""
        return f"Imagem ID {self.id}{descricao_display} - Registro {self.registro.id}"


class retorno(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='clientes')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='produtos')
    tipo_problema = models.CharField(max_length=100, choices=[
        ('Oxidação', 'Oxidação'),
        ('Placa Danificada', 'Placa Danificada'),
        ('Placa danificada SEM CUSTO', 'Placa danificada SEM CUSTO'),
        ('USB Danificado', 'USB Danificado'),
        ('USB Danificado SEM CUSTO', 'USB Danificado SEM CUSTO'),
        ('Botão de acionamento Danificado', 'Botão de acionamento Danificado'),
        ('Botão de acionamento Danificado SEM CUSTO', 'Botão de acionamento Danificado SEM CUSTO'),
        ('Antena LoRa Danificada', 'Antena LoRa Danificada'),
        ('Sem problemas Identificados', 'Sem problemas Identificados'),
    ])
    imagem = models.ImageField(upload_to='imagens/')
    id_equipamentos = models.TextField(max_length=250, blank=True, default='')

    def __str__(self):
        return f"{self.cliente} - {self.produto} - {self.tipo_problema}"