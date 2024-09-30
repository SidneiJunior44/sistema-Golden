from django.db import models
from acompanhamento.models import Clientes

class Reativacao(models.Model):
    STATUS_CHOICES = [
        ('', 'Selecione o Status'),
        ('Vazio', 'Vazio'),
        ('faturado', 'Faturado'),
    ]

    nome = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='reativacao_nome')
    motivo_reativacao = models.CharField(null=True, blank=True, max_length=50)
    canal_solicitacao = models.CharField(max_length=100, null=True, blank=True)
    observacoes = models.CharField(max_length=100)
    status_reativacao = models.CharField(max_length=10, choices=STATUS_CHOICES, default='')

    def __str__(self):
        return f"Reativacao {self.id} - {self.nome}"

class IdIccid(models.Model):
    reativacao = models.ForeignKey(Reativacao, on_delete=models.CASCADE, related_name='id_iccids')
    id_equipamentos = models.CharField(max_length=300, blank=True, default='')
    ccid_equipamentos = models.CharField(max_length=300, blank=True, default='')

    def __str__(self):
        return f"IdIccid {self.id} - ID: {self.id_equipamentos}, ICCID: {self.ccid_equipamentos}"
