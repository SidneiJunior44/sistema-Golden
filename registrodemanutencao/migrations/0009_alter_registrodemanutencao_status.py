# Generated by Django 5.0.7 on 2024-09-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrodemanutencao', '0008_alter_imagemregistro_setorid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrodemanutencao',
            name='status',
            field=models.CharField(blank=True, choices=[('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado'), ('Pendente', 'Pendente'), ('Expedição', 'Expedição'), ('expedido', 'expedido')], default='Pendente', max_length=50, null=True),
        ),
    ]