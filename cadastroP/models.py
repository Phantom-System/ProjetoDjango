from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome