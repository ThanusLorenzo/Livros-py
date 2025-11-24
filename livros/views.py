# livros/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm # Requer que o arquivo forms.py seja carregado

# 1. READ (Listar todos os livros)
def listar_livros(request):
    livros = Livro.objects.all()
    # ✅ Garante que o template correto 'listar_livros.html' está sendo usado
    return render(request, 'livros/listar_livros.html', {'livros': livros})

# 2. CREATE (Adicionar novo livro)
def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/criar_livro.html', {'form': form})

# 3. UPDATE (Editar livro existente)
def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/editar_livro.html', {'form': form, 'livro': livro})

# 4. DELETE (Excluir livro)
def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'livros/deletar_livro.html', {'livro': livro})