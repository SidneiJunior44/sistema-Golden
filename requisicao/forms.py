from django import forms
from .models import Requisicoes, Clientes
from datetime import datetime

class requisicaoForm(forms.ModelForm):
    class Meta:
        model = Requisicoes
        fields = ['nome', 'endereco', 'contrato', 'cnpj', 'inicio_de_contrato', 'vigencia', 'data',
                  'motivo', 'envio', 'comercial', 'tipo_produto', 
                  'carregador', 'cabo', 'tipo_fatura', 'valor_unitario', 'valor_total',
                  'forma_pagamento', 'observacoes', 'status', 'TP', 'taxa_envio','status_faturamento', 'id_equipamentos']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'contrato': forms.Select(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'inicio_de_contrato': forms.DateInput(attrs={'class': 'form-control'}),
            'vigencia': forms.DateInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control'}),
            'motivo': forms.Select(attrs={'class': 'form-control'}),
            'comercial': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_produto': forms.Select(attrs={'class': 'form-control'}),
            'envio': forms.Select(attrs={'class': 'form-control'}),
            'taxa_envio': forms.NumberInput(attrs={'class': 'form-control'}),
            'carregador': forms.TextInput(attrs={'class': 'form-control'}),
            'cabo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_fatura': forms.Select(attrs={'class': 'form-control'}),
            'valor_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'forma_pagamento': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'TP': forms.Select(attrs={'class': 'form-control'}),
            'status_faturamento': forms.Select(attrs={'class': 'form-control'}),
            'id_equipamentos': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
        permissions = [
            ("view_requisicoes", "Can view requisicoes"),
            ("add_requisicoes", "Can add requisicoes"),
            ("change_requisicoes", "Can change requisicoes"),
            ("delete_requisicoes", "Can delete requisicoes"),
        ]

    def __init__(self, *args, **kwargs):
        editable_fields = kwargs.pop('editable_fields', None)
        super().__init__(*args, **kwargs)
        self.fields['nome'].queryset = Clientes.objects.all()
        self.fields['nome'].empty_label = "Selecione um cliente"

        if editable_fields:
            for field_name in self.fields:
                if field_name not in editable_fields:
                    self.fields[field_name].widget.attrs['readonly'] = 'readonly'
