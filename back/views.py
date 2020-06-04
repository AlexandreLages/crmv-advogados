from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from core.models import Advogado
from core.models import PaginaInicial


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['senha']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            advogado = Advogado.objects.get(user=user)
            return redirect('/advogado/', {'message': 'Usuário logado com sucesso!'})
        else:
            return render(request, 'login.html', {'message': 'Usuário/Senha inválidos!'})


def logout_view(request):
	logout(request)
	return redirect('/')


@login_required
def advogado_view(request):
    advogado = Advogado.objects.get(user=request.user)
    return render(request, 'advogado.html', {'advogado': advogado})


@login_required
def dash_home_view(request):
    advogado = Advogado.objects.get(user=request.user)
    home = PaginaInicial.objects.all()
    if home:
        home = PaginaInicial.objects.filter()[0]
    return render(request, 'dash_pagina_inicial.html', {'advogado': advogado, 'home': home})    