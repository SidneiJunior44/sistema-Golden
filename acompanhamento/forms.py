# acompanhamento/forms.py
from django import forms
from .models import Clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'endereco', 'cnpj','inicio_de_contrato','vigencia','termino','status','equipamento','quantidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'inicio_de_contrato': forms.TextInput(attrs={'class': 'form-control'}),
            
            'vigencia': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'termino': forms.Textarea(attrs={'class' : 'form-control', 'rows':1}),
            'equipamento': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.Textarea(attrs={'class' : 'form-control', 'rows':1}),
        }
