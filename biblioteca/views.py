from django import http
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Libros
from .forms import LibrosForm

#Vamo a importar el modelo para poder leer los datos de nuestra base de datos
# Creamos una peticion la cual nos respode con un saludo

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

# creamos una variable e importamos todos los objetos
def libros(request):
    libro = Libros.objects.all()
    return render(request, 'libros/index.html', {'libro': libro})

def crear(request):
    formulario  =  LibrosForm(request.POST or None, request.FILES or None)
    #Preguntamos si el formulario es valido y guardar la info
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request, id):
    libro = Libros.objects.get(id = id)
    formulario = LibrosForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario' : formulario})

def eliminar(request, id):
    libro = Libros.objects.get(id = id)
    libro.delete()
    return redirect('libros')
