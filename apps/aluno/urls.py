from django.urls import path
from apps.aluno.views import index, listar, cadastrar

urlpatterns = [
    path("", index, name="index"),
    path("lista", listar, name="aluno/lista"),
    path("cadastro", cadastrar, name="aluno/cadastro")

]