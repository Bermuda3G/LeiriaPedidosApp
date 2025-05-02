from django.db import models
from produtos.models import Produto

# Create your models here.
class Pedido(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    nome_cliente = models.CharField(max_length=100)
    telefone_cliente = models.CharField(max_length=15)
    endereco_entrega = models.CharField(max_length=255)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    data_entrega = models.DateField(null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Pedido #{self.id} - "

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} no Pedido #{self.pedido.id}"