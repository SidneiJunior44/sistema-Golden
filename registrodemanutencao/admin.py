from django.contrib import admin
from .models import registrodemanutencao  # Importa o modelo registrodemanutencao.

# Classe para personalizar a exibição do modelo registrodemanutencao no admin.
class RegistroDeManutencaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_produto', 'motivo', 'faturamento', 'customizacao',
                    'entregue_por_retirado_por', 'numero_equipamento', 'tratativa', 'imagem',
                    'manutencaoequipamentos', 'retornoequipamentos', 'setor')
    search_fields = ('nome',)  # Permite a busca pelo campo 'nome'.

    # Método para exibir a imagem no admin. (Aqui você pode adicionar lógica para exibir uma miniatura)
    def imagen(self, obj):
        return obj.imagem

# Registra o modelo registrodemanutencao com a classe RegistroDeManutencaoAdmin personalizada.
admin.site.register(registrodemanutencao, RegistroDeManutencaoAdmin)