# Generated by Django 5.0.7 on 2024-08-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acompanhamento', '0009_rename_cliente_clientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='status',
            field=models.CharField(blank=True, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='termino',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='vigencia',
            field=models.CharField(blank=True, choices=[('', ''), ('12', '12'), ('24', '24'), ('36', '36'), ('48', '48')], max_length=50, null=True),
        ),
    ]
