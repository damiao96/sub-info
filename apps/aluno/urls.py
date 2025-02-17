from django.urls import path
from apps.aluno.views import index

urlpatterns = [
    path("", index, name="index")
]