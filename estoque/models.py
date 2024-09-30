from django.db import models
from produto.models import Produto
from django.utils import timezone
class estoque(models.Model):
    nome = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='estoque_produto')
    marca = models.TextField(max_length=50 , null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    descricao = models.TextField()
    preco = models.IntegerField(null=True, blank=True)
    data_criacao = models.DateTimeField(editable=False,null=True)
   


    def save(self, *args, **kwargs):
        if not self.id:
            self.data_saida = timezone.now()
        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.nome)