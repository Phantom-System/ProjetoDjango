from django.urls import path
from .views import cadastrar_produto, exibir_produtos


urlpatterns = [
    path('', cadastrar_produto),
    path('lista_produtos/', exibir_produtos)
]
