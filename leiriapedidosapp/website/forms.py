from django import forms
from django.forms import ModelForm
from .models import Produto, Pedido, ItemPedido

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

class PedidoForm_1(ModelForm):
    class Meta:
        model = Pedido
        fields = ('nome_cliente', 'numero_cliente', 'endereco_cliente', 'endereco_entrega')
        labels = {
            'nome_cliente': 'Nome do Cliente',
            'numero_cliente': 'Número do Cliente',
            'endereco_cliente': 'Endereço do Cliente',
            'endereco_entrega': 'Endereço de Entrega'
        }
        widgets = {
            'nome_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_cliente': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'endereco_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco_entrega': forms.TextInput(attrs={'class': 'form-control'}),
        }
