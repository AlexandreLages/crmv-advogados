from django.shortcuts import render

from core.models import PaginaInicial


def index(request):
	home = PaginaInicial.objects.all()
	if home:
		home = PaginaInicial.objects.filter()[0]
		return render(request, 'index.html', {'home': home})
	return render(request, 'index.html')