# Generated by Django 5.0.7 on 2024-09-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualit',
            name='observacoes',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
