# Generated by Django 5.0.7 on 2024-08-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0017_requisicoes_status_faturamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicoes',
            name='motivo',
            field=models.CharField(blank=True, choices=[('', ''), ('Aquisicão Nova', 'Aquisicão Nova'), ('Manutenção', 'Manutenção'), ('Aditivo', 'Aditivo'), ('Acessorios', 'Acessorios'), ('Extravio', 'Extravio'), ('Texte', 'Texte'), ('Isca Fast', 'Isca Fast'), ('Isca Fast Agente', 'Isca Fast Agente'), ('Antenista', 'Antenista'), ('Reversa', 'Reversa')], default='', max_length=50, null=True),
        ),
    ]
