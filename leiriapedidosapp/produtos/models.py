from django.db import models

# Create your models here.
class Produto(models.Model):
    CATEGORIA_CHOICES = [
        ('BOLO', 'Bolo'),
        ('DOCE', 'Doce'),
        ('SALGADO', 'Salgado'),
        ('TORTA', 'Torta'),
        ('MASSA', 'Massa'),
    ]
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    preco_unitario = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Preço Unitário')
    preco_kg = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Preço por Kg')

    def __str__(self):
        return self.nome