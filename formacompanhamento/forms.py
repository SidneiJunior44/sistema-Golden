from django import forms
from .models import Formacompanhamento
import datetime

# Não é necessário importar Cliente aqui, a menos que seja usado em outro lugar do código.

class formacompanhamentoForm(forms.ModelForm):
    class Meta:
        model = Formacompanhamento
        fields = ['data_inicio', 'data_final', 'prestador', 'agente', 'placa','id_equipamento','km_inicial','km_final','pedagio']
        widgets = {
            'data_inicio': forms.DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'data_final': forms.DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'prestador': forms.Select(attrs={'class': 'form-control'}),
            'agente': forms.TextInput(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),
            'id_equipamento': forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),
            'km_inicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'km_final': forms.NumberInput(attrs={'class': 'form-control'}),
            'pedagio':forms.NumberInput(attrs={'class': 'form-control'}),
            
        }


        