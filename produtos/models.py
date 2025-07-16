from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(
        auto_now_add=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome