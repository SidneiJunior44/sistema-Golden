from django.db import models

class Rprestador(models.Model):
    nome = models.CharField(max_length=100)  # Campo de texto com comprimento máximo de 100
    franquia_km = models.TextField(max_length=50, null=True, blank=True)  # Campo de texto que pode ser deixado em branco
    franquiah = models.TimeField()  # Campo de tempo
    valor_acionamento = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Campo decimal com 2 casas decimais
    valorkm = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Campo decimal com 2 casas decimais
    valor_exedente = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Campo decimal com 2 casas decimais
    
    def __str__(self):
        return self.nome  # A representação de string deste objeto será o valor do campo 'nome'
