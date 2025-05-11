from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    observacoes = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome
    
class PrdutoSalgado(Produto):
