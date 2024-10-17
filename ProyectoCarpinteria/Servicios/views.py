from django.shortcuts import render
from .models import Categoria, ProductosLavadora
from .modelp import Temas, ProgrammingTopics


# Create your views here.


def Categorias(request):
    objetos = Categoria.objects.all()
    return render(request, "serv/servicios.html", {"categorias": objetos})


def ProductosLavadoraView(request, pk):
    todas = Categoria.objects.get(pk=pk)
    lavadoras = ProductosLavadora.objects.filter(categoria=todas)
    return render(request, "lavadoras/lavadoras.html", {"lavadoras": lavadoras, "todas": todas})


def ProgrammingTopicsView(request, pk):

    categoriaP = Categoria.objects.get(pk=pk)
    temas = ProgrammingTopics.objects.filter(categoria=categoriaP)
    return render(request, "programming/programming.html", {"temas": temas, "categorias": categoriaP})
