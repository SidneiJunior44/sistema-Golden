from django import forms
from .models import estoque
import datetime

# Não é necessário importar Cliente aqui, a menos que seja usado em outro lugar do código.

class estoqueForm(forms.ModelForm):
    class Meta:
        model = estoque
        fields = ['nome', 'descricao', 'preco', 'marca', 'quantidade']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            
            
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            
        
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
        }