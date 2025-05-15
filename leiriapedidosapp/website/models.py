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
    oberservacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return(f"{self.nome}")