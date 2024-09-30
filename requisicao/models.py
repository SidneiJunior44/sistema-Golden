from django.db import models
from acompanhamento.models import Clientes   
from produto.models import Produto    

class Requisicoes(models.Model):
    # Definição das escolhas de status
    statuschoice = [
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
        ('Pendente', 'Pendente'),
        ('Configurado', 'Configurado'),
        ('Expedido', 'Expedido'),
    ]

    # Definição das escolhas de TP (tempo de processamento)
    TP = [
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('30', '30'),
        ('60', '60'),
        ('360', '360'),
        ('720', '720'),
    ]
    statusfat = [
        ('', ''),
        ('A Faturar', 'A Faturar'),
        ('Faturado sem Taxa', 'Faturado sem Taxa'),
        ('Faturado com Taxa', 'Faturado com Taxa'),
        ('Pendente', 'Pendente'),
        ('Pendente sem Contrato', 'Pendente sem Contrato'),
        ('Pendente Sem Termo', 'Pendente Sem Termo'),
        ('Pendente Sem Contrato', 'Pendente Sem Contrato'),
        ('Sem Custo', 'Sem Custo'),
        ('Dados invalidos', 'Dados invalidos'),
    ]
    motivoc = [
        ('Tipo de Faturamento', 'Tipo de Faturamento'),
        ('Aquisicão Nova', 'Aquisicão Nova'),
        ('Manutenção', 'Manutenção'),
        ('Aditivo', 'Aditivo'),
        ('Acessorios', 'Acessorios'),
        ('Extravio', 'Extravio'),
        ('Texte', 'Texte'),
        ('Isca Fast', 'Isca Fast'),
        ('Isca Fast Agente', 'Isca Fast Agente'),
        ('Antenista', 'Antenista'),
        ('Reversa', 'Reversa'),
    ]

    # Definição das escolhas de tipo de envio
    tipo_envio = [
        ('Agente', 'Agente'),
        ('Retirada', 'Retirada'),
        ('Motoboy', 'Motoboy'),
        ('transportadora', 'Transportadora'),
        ('Correio', 'Correio'),
        ('Comercial', 'Comercial'),
    ]

    # Definição das escolhas de tipo de contrato
    contrato_tipo = [
        ('', ''),
        ('Descartavel', 'Descartavel'),
        ('Retornavel', 'Retornavel'),
    ]

    # Definição das escolhas de tipo de fatura
    fatura_tipo = [
        ('Com Custo', 'Com Custo'),
        ('Sem Custo', 'Sem Custo'),
    ]

    # Definição das escolhas de status
    STATUS_CHOICES = [
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
        ('Pendente', 'Pendente'),
        ('Configurado', 'Configurado'),
        ('Reprovado pelo CEO', 'Reprovado pelo CEO'),
        ('Aprovado pelo CEO', 'Aprovado pelo CEO'),
        ('Reprovado pela Diretoria', 'Reprovado pela Diretoria'),
        ('Aprovado pela Diretoria', 'Aprovado pela Diretoria'),
        ('Enviado para o Cliente', 'Enviado para o Cliente'),
    ]

    # Campos do modelo
    nome = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='requisicoes_nome')
    endereco = models.CharField(max_length=255, blank=True, null=True)
    contrato = models.CharField(choices=contrato_tipo, null=True, blank=True, max_length=50)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    inicio_de_contrato = models.DateField(blank=True, null=True)
    vigencia = models.DateField(blank=True, null=True)
    data = models.DateField()
    motivo = models.CharField(choices=motivoc,  default='', null=True, blank=True, max_length=50)
    envio = models.CharField(choices=tipo_envio, null=True, blank=True, max_length=50)
    taxa_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    comercial = models.CharField(max_length=100, blank=True, default='')
    tipo_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='requisicoes_produto')
    carregador = models.CharField(max_length=100, blank=True, default='')
    cabo = models.CharField(max_length=100, blank=True, default='')
    tipo_fatura = models.CharField(choices=fatura_tipo, null=True, blank=True, max_length=50)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    forma_pagamento = models.CharField(max_length=100, blank=True, default='')
    observacoes = models.TextField(max_length=250, blank=True, default='')
    status = models.CharField(default='Pendente', null=True, blank=True, max_length=50)
    TP = models.CharField(choices=TP, null=True, blank=True, max_length=50)
    status_faturamento = models.CharField(choices=statusfat,  default="Selecione o status do faturamento",null=True, blank=True, max_length=50)
    id_equipamentos= models.TextField(max_length=250, blank=True, default='')
    def __str__(self):
        return f"Requisição {self.id} - {self.nome}"
