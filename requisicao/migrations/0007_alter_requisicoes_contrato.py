# Generated by Django 5.0.7 on 2024-08-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0006_alter_requisicoes_tp_alter_requisicoes_tipo_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicoes',
            name='contrato',
            field=models.CharField(blank=True, choices=[('', ''), ('Descartavel', 'Descartavel'), ('Retornavel', 'Retornavel')], default='', max_length=50, null=True),
        ),
    ]