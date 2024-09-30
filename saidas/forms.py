from typing import Any
from django import forms
from .models import saidas
from django.utils import timezone
from django.core.exceptions import ValidationError

# Não é necessário importar Cliente aqui, a menos que seja usado em outro lugar do código.

class saidasForm(forms.ModelForm):
    class Meta:
        model = saidas
        fields = ['nome', 'descricao','preco', 'marca', 'quantidade']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'descrição': forms.TextInput(attrs={'class': 'form-control'}),
            
            
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            
        
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
    
        }

    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        nome = self.cleaned_data.get('nome')

        if quantidade  > nome.quantidade:
            raise ValidationError(
                f'A quantidade disponivel do produto {nome.nome} é de {nome.quantidade} unidades '

            )
        return quantidade