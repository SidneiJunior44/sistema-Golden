# Generated by Django 5.0.7 on 2024-08-19 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saidas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saidas',
            name='descricao',
        ),
    ]
