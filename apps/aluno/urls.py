from django.urls import path
from apps.aluno.views import index, imagem, listar

urlpatterns = [
    path("", index, name="index"),
    path("imagem/", imagem, name="imagem"),
    path("lista", listar, name="aluno/lista")
]