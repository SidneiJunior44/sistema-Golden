# Generated by Django 5.0.7 on 2024-08-27 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0014_alter_requisicoes_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicoes',
            name='status',
            field=models.CharField(blank=True, choices=[('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado'), ('Pendente', 'Pendente')], default='Pendente', max_length=50, null=True),
        ),
    ]