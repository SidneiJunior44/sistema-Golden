# Generated by Django 5.0.7 on 2024-08-14 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0009_alter_requisicoes_envio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisicoes',
            name='tipo_acesso',
        ),
    ]