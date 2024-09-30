# Generated by Django 5.0.7 on 2024-08-19 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0004_produto_marca_produto_quantidade_alter_produto_preco'),
    ]

    operations = [
        migrations.CreateModel(
            name='saidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.TextField(blank=True, max_length=50, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('descricao', models.TextField()),
                ('preco', models.IntegerField(blank=True, null=True)),
                ('data_criacao', models.DateTimeField(editable=False, null=True)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='saida_produto', to='produto.produto')),
            ],
        ),
    ]
