from django.contrib import admin

# Register your models here.
from . import models 

class saidasadmin(admin.ModelAdmin):
    list_display = ('nome','data_criacao', 'descricao')
    search_fields = ('nome',)

admin.site.register(models.saidas,saidasadmin)
