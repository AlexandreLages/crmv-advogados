from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

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

    if request.method == 'GET':
        return render(request, 'dash_pagina_inicial.html', {'advogado': advogado, 'home': home})

    elif request.method == 'POST':
        if home:
            home.titulo = request.POST['titulo_site']
            home.titulo_sobre = request.POST['titulo_sobre']
            home.mensagem_sobre = request.POST['mensagem_sobre']
            home.email_principal = request.POST['email_principal']
            home.telefone_principal = request.POST['telefone_principal']
            imagem_sobre = request.FILES.get('imagem_sobre', False)

            if imagem_sobre:
                fs = FileSystemStorage()
                filename = fs.save(imagem_sobre.name, imagem_sobre)
                uploaded_file_url = fs.url(filename)
                home.imagem_sobre=uploaded_file_url

            home.save()

        return render(request, 'dash_pagina_inicial.html', {'advogado': advogado, 'home': home})


@login_required
def dash_redes_view(request):
    advogado = Advogado.objects.get(user=request.user)
    home = PaginaInicial.objects.all()

    if home:
        home = PaginaInicial.objects.filter()[0]

    if request.method == 'POST':
        if home:
            home.titulo = request.POST['titulo_site']
            home.titulo_sobre = request.POST['titulo_sobre']
            home.mensagem_sobre = request.POST['mensagem_sobre']
            imagem_sobre = request.FILES.get('imagem_sobre', False)

            if imagem_sobre:
                fs = FileSystemStorage()
                filename = fs.save(imagem_sobre.name, imagem_sobre)
                uploaded_file_url = fs.url(filename)
                home.imagem_sobre=uploaded_file_url

            home.save()

        return render(request, 'dash_pagina_inicial.html', {'advogado': advogado, 'home': home})
