# Generated by Django 5.0.7 on 2024-08-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0008_alter_requisicoes_tp_alter_requisicoes_contrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicoes',
            name='envio',
            field=models.CharField(blank=True, choices=[('Agente', 'Agente'), ('Retirada', 'Retirada'), ('Motoboy', 'Motoboy'), ('transportadora', 'Transportadora'), ('Correio', 'Correio'), ('Comercial', 'Comercial')], max_length=50, null=True),
        ),
    ]
