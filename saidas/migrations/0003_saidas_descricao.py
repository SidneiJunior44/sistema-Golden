# Generated by Django 5.0.7 on 2024-08-19 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saidas', '0002_remove_saidas_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='saidas',
            name='descricao',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]