# tarefas/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'tarefas/lista_projetos.html', {'projetos': projetos})

def cadastrar_projeto(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_projetos')
    return render(request, 'tarefas/form_projeto.html', {'form': form})

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})

def cadastrar_tarefa(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_tarefas')
    return render(request, 'tarefas/form_tarefa.html', {'form': form})

def editar_projeto(request, id):
    projeto = Projeto.objects.get(id=id)
    form = ProjetoForm(request.POST or None, instance=projeto)
    if form.is_valid():
        form.save()
        messages.success(request, 'Projeto atualizado com sucesso!')
        return redirect('lista_projetos')
    return render(request, 'tarefas/form_projeto.html', {'form': form, 'editar': True})

def editar_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tarefa atualizada com sucesso!')
        return redirect('lista_tarefas')
    return render(request, 'tarefas/form_tarefa.html', {'form': form, 'editar': True})