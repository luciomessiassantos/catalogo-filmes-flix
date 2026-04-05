from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from django.http import HttpRequest
from .models import *
# Create your views here.

def HomePage(request: HttpRequest):

    movies = Filme.objects.all()
    destaque = Filme.objects.first()
    categorias_validas = Categoria.objects.prefetch_related(
        Prefetch('filmes', queryset=Filme.objects.order_by('-ano_lancamento'))
    ).order_by('nome').all()

    filmes_carrossel = {}

    for categoria in categorias_validas:
        nome_display = categoria.get_nome_display() # type: ignore
        filmes_categoria = categoria.filmes.all() # type: ignore
        print(filmes_categoria) # type: ignore
        if filmes_categoria:
            filmes_carrossel[nome_display] = filmes_categoria

    context = {
        "movies": movies,
        "destaque": destaque,
        "carrossel": filmes_carrossel
    }

    return render(request, 'home.html', context)

def Details(request: HttpRequest, id):
    filme = get_object_or_404(Filme, id=id)
    
    return render(request, 'details.html', {"filme": filme})

