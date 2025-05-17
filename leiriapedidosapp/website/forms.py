from django import forms
from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'medido_por', 'preco', 'observacoes')
        labels = {
            'nome': 'Nome',
            'medido_por': 'Unidade de Medida',
            'preco': 'Preço',
            'observacoes': 'Observações'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'medido_por': forms.Select(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
        }