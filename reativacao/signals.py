# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Reativacao

@receiver(post_save, sender=Reativacao)
def enviar_email_requisicao_criada(sender, instance, created, **kwargs):
    if created:
        subject = f"Nova Reativação: {instance.id}"
        message = f"A nova reativação {instance.id} foi criada com sucesso. {instance.nome} "
        from_email = 'sysggoldensat@gmail.com'
        recipient_list = ['sjuniorr6@gmail.com']
        
        send_mail(subject, message, from_email, recipient_list)
