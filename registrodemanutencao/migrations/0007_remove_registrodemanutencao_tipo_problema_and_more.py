# Generated by Django 5.0.7 on 2024-08-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrodemanutencao', '0006_imagemregistro_setorid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrodemanutencao',
            name='tipo_problema',
        ),
        migrations.AddField(
            model_name='imagemregistro',
            name='tipo_problema',
            field=models.CharField(blank=True, choices=[('Oxidação', 'Oxidação'), ('Placa Danificada', 'Placa Danificada'), ('Placa danificada SEM CUSTO', 'Placa danificada SEM CUSTO'), ('USB Danificado', 'USB Danificado'), ('USB Danificado SEM CUSTO', 'USB Danificado SEM CUSTO'), ('Botão de acionamento Danificado', 'Botão de acionamento Danificado'), ('Botão de acionamento Danificado SEM CUSTO', 'Botão de acionamento Danificado SEM CUSTO'), ('Antena LoRa Danificada', 'Antena LoRa Danificada'), ('Sem problemas Identificados', 'Sem problemas Identificados')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='imagemregistro',
            name='setorid',
            field=models.CharField(blank=True, choices=[('expedicao', 'expedicao'), ('Manutenção', 'Manutenção'), ('configuração', 'configuração')], default='', max_length=50, null=True),
        ),
    ]
