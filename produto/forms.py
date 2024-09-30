from django import forms
from .models import Produto

# Não é necessário importar Cliente aqui, a menos que seja usado em outro lugar do código.

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'marca', 'quantidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
          
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
        }