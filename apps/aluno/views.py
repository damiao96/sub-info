from django.shortcuts import render, redirect, get_object_or_404
from apps.aluno.models import Aluno
from apps.aluno.forms import AlunoForms

def index(request):
    return render(request, 'aluno/index.html')

def listar(request):
    alunos = Aluno.objects.order_by("-id")

    return render(request, "aluno/lista.html", {"alunos": alunos})

def cadastrar(request):
    form = AlunoForms()

    if request.method == 'POST':
        form = AlunoForms(request.POST)
        if form.is_valid:
            form.save()
            return redirect("aluno/lista")

    return render(request, "aluno/cadastro.html", {"form": form})

def editar(request, id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForms(instance=aluno)

    if request.method == 'POST':
        form = AlunoForms(request.POST, instance=aluno)
        if form.is_valid:
            form.save()
            return redirect("aluno/lista")

    return render(request, "aluno/cadastro.html", {"form": form})

    return render(request, "aluno/edita.html", {"form": form,  "aluno_id": id})

def exibir(request, id):
    aluno= get_object_or_404(Aluno, pk=id)
    return render(request, "aluno/exibe.htmkl", {"aluno": aluno})