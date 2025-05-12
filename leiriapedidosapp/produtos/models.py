from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    observacoes = models.TextField(null=True, blank=True)
    preco_unidade = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Preço por unidade',
        blank=True,
        null=True
    )
    preco_cento = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Preço por Cento',
        blank=True,
        null=True
    )
    preco_kg = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Preço por Kg',
        blank=True,
        null=True
    )

    def clean(self):
        from django.core.exceptions import ValidationError
        precos_preenchidos = sum(1 for preco in [self.preco_unidade, self.preco_cento, self.preco_kg] if preco is not None)
        if precos_preenchidos > 1:
            raise ValidationError("Preencha apenas um dos campos de preço (Unidade, Cento ou Kg).")
        elif self.preco_cento is not None and self.preco_unidade is None:
            self.preco_unidade = self.preco_cento / 100
        elif self.preco_unidade is not None:
            self.preco_cento = None
            self.preco_kg = None
        elif self.preco_kg is not None:
            self.preco_unidade = None
            self.preco_cento = None

        super().clean()

    def __str__(self):
        return self.nome