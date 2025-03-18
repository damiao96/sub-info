from django.shortcuts import render
from apps.aluno.models import Aluno
from apps.aluno.forms import AlunoForms

def index(request):
    return render(request, 'aluno/index.html')

def listar(request):
    alunos = Aluno.objects.order_by("nome")

    return render(request, "aluno/lista.html", {"alunos": alunos})

def cadastrar(request):
    form = AlunoForms()
    return render(request, "aluno/cadastro.html", {"form": form})