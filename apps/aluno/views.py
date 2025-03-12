from django.shortcuts import render
from apps.aluno.models import Aluno

def index(request):
    return render(request, 'aluno/index.html')


def imagem(request):
    return render(request, 'aluno/imagem.html')

def listar(request):
    alunos = Aluno.objects.order_by("nome")

    return render(request, "aluno/lista.html", {"alunos": alunos})