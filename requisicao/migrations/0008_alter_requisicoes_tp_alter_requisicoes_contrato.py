# Generated by Django 5.0.7 on 2024-08-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0007_alter_requisicoes_contrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicoes',
            name='TP',
            field=models.CharField(blank=True, choices=[('5', '5'), ('10', '10'), ('15', '15'), ('30', '30'), ('60', '60'), ('360', '360'), ('720', '720')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='requisicoes',
            name='contrato',
            field=models.CharField(blank=True, choices=[('', ''), ('Descartavel', 'Descartavel'), ('Retornavel', 'Retornavel')], max_length=50, null=True),
        ),
    ]
