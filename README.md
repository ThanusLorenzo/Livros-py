# 📚 Projeto Biblioteca CRUD (Django + SQLite)

Este é um projeto simples desenvolvido em Django para demonstrar as operações básicas de **CRUD** (Create, Read, Update, Delete) em um banco de dados **SQLite**, gerenciando um cadastro de livros.

## ✨ Funcionalidades

O aplicativo `livros` permite:

* **Listar (READ):** Visualizar todos os livros cadastrados.
* **Criar (CREATE):** Adicionar um novo livro com título, autor e ano de publicação.
* **Editar (UPDATE):** Modificar os dados de um livro existente.
* **Deletar (DELETE):** Remover um livro do cadastro.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para clonar, configurar e executar a aplicação em sua máquina local.

### Pré-requisitos

Você deve ter o **Python** (versão 3.x) e o **Git** instalados.

### 1. Clonar o Repositório

```bash
git clone [https://github.com/SeuUsuario/Nome-Do-Repositorio.git](https://github.com/SeuUsuario/Nome-Do-Repositorio.git)
cd biblioteca_crud

### 2. Configurar o Ambiente
Recomendamos o uso de um ambiente virtual (venv):

Bash

# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Linux/macOS)
source venv/bin/activate

# Ativa o ambiente virtual (Windows)
# venv\Scripts\activate

### 3. Instalar Dependências
Instale o Django (e quaisquer outras dependências futuras):

Bash

pip install django

### 4. Aplicar Migrações
O Django usará o SQLite por padrão para criar a tabela Livro no arquivo db.sqlite3.

Bash

python manage.py makemigrations livros
python manage.py migrate

### 5. Iniciar o Servidor
Bash

python manage.py runserver
O projeto estará acessível em: http://127.0.0.1:8000/livros/

📁 Estrutura do Projeto
A estrutura principal do aplicativo de gerenciamento de livros é a seguinte:

biblioteca_crud/
├── biblioteca_crud/       # Configurações do Projeto
├── livros/                # App CRUD de Livros
│   ├── models.py          # Define o modelo Livro
│   ├── forms.py           # Define o formulário LivroForm
│   ├── views.py           # Contém a lógica CRUD (listar, criar, editar, deletar)
│   ├── urls.py            # Define as rotas do app
│   └── templates/
│       └── livros/
│           ├── listar_livros.html  # READ
│           ├── criar_livro.html    # CREATE
│           ├── editar_livro.html   # UPDATE
│           └── deletar_livro.html  # DELETE
└── manage.py
🤝 Contribuições
Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto!

Autor: Thânus Alves
