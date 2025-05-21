from django.db import models

# Create your models here.
class Produto(models.Model):
    MEDIDO_POR_CHOICES = [
        ('UNIDADE', 'Unidade'),
        ('CENTO', 'Cento'),
        ('QUILO', 'Quilo')
    ]

    nome = models.CharField(max_length=50)
    medido_por = models.CharField(
        max_length=10,
        choices=MEDIDO_POR_CHOICES,
        default='UNIDADE'
    )
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    observacoes = models.TextField(max_length=75, blank=True, null=True)

    def __str__(self):
        return(f"{self.nome}")
    
class Pedido(models.Model):
    nome_cliente = models.CharField(max_legnth=50)
    numero_cliente = models.CharField(max_length=20)
    endereco_cleinte = models.TextField(max_length=100)
    endereco_entrega = models.TextField(max_length=100)
    produtos = models.ManyToManyField(Produto, through="ItemPedido")
    valor = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)
    observacoes = models.TextField(max_length=100)

    def __str__(self):
        return(f"Pedido #{self.id}")
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Produto, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return(f"{self.produto.nome} X {self.quantidade}")