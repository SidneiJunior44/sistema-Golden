# Generated by Django 5.0.7 on 2024-09-09 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrodemanutencao', '0013_alter_retorno_cliente_alter_retorno_produto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='retorno',
            old_name='descricao',
            new_name='id_equipamentos',
        ),
    ]
