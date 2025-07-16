from django.shortcuts import render
from .models import Produto

# Create your views here.

def lista_produtos(request):
    produtos = Produto.objects.filter(
        ativo=True).order_by('nome')
    return render(request, 'produtos_em_estoque.html', {'produtos': produtos})