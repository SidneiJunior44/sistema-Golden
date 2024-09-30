from django.contrib import admin

# Register your models here.
from . import models 

class aclientesadmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco','cnpj','inicio_de_contrato','vigencia')
    search_fields = ('nome',)

admin.site.register(models.Clientes,aclientesadmin)