from django.db.models.signals import post_save
from django.dispatch import receiver
from estoque.models import estoque

@receiver(post_save, sender=estoque)
def atualizacao_Produto(sender, instance, created, **kwargs):
    if created:
        produto = instance.nome  # obtenha o objeto do produto associado ao estoque
        produto.quantidade += instance.quantidade
        produto.save()