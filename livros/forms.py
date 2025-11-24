from django import forms
from .models import Livro # ✅ Use esta importação relativa

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano_publicacao']