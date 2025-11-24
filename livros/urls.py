# livros/urls.py

from django.urls import path
from . import views # ✅ Importação relativa correta

urlpatterns = [
    # Rota para LISTAGEM (READ) - name='listar_livros' (corrigido para o que você usa nos outros templates)
    path('', views.listar_livros, name='listar_livros'),
    
    # Rota para CRIAÇÃO (CREATE) - name='criar_livro' (resolve o NoReverseMatch)
    path('novo/', views.criar_livro, name='criar_livro'),
    
    # Rota para EDIÇÃO (UPDATE)
    path('editar/<int:pk>/', views.editar_livro, name='editar_livro'),
    
    # Rota para DELEÇÃO (DELETE)
    path('deletar/<int:pk>/', views.deletar_livro, name='deletar_livro'),
]