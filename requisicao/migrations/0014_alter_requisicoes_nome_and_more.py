# Generated by Django 5.0.7 on 2024-08-20 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acompanhamento', '0010_clientes_status_clientes_termino_and_more'),
        ('produto', '0004_produto_marca_produto_quantidade_alter_produto_preco'),
        ('requisicao', '0013_alter_requisicoes_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicoes',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisicoes_nome', to='acompanhamento.clientes'),
        ),
        migrations.AlterField(
            model_name='requisicoes',
            name='tipo_produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisicoes_produto', to='produto.produto'),
        ),
    ]