# tarefas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('projetos/novo/', views.cadastrar_projeto, name='cadastrar_projeto'),
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefas/nova/', views.cadastrar_tarefa, name='cadastrar_tarefa'),
    path('projetos/editar/<int:id>/', views.editar_projeto, name='editar_projeto'),
    path('tarefas/editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
]