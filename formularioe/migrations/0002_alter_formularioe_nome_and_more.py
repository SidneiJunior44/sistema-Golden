# Generated by Django 5.0.7 on 2024-08-21 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acompanhamento', '0010_clientes_status_clientes_termino_and_more'),
        ('formularioe', '0001_initial'),
        ('produto', '0004_produto_marca_produto_quantidade_alter_produto_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioe',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formularioe_nome', to='acompanhamento.clientes'),
        ),
        migrations.AlterField(
            model_name='formularioe',
            name='tipo_produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formularioe_produto', to='produto.produto'),
        ),
    ]
