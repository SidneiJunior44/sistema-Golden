from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.TextField(null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    descricao = models.TextField()
    preco = models.IntegerField(null=True, blank=True)
   
    def __str__(self):
     return self.nome
