# Generated by Django 5.0.7 on 2024-09-09 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0026_alter_requisicoes_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisicoes',
            name='taxa_envio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
