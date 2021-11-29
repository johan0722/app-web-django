from django.shortcuts import render
from django.http import HttpResponse
from .models import Libros

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
    return render(request, 'libros/crear.html')

def editar(request):
    return render(request, 'libros/editar.html')
