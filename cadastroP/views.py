from django.shortcuts import render, redirect
from .models import Produto

# Create your views here.

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')

        Produto.objects.create(
            nome=nome,
            preco=preco,
            descricao=descricao
        )
        return redirect('lista_produtos/')
    return render(request, 'cadastro_produtos.html')

def exibir_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})


