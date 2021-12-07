from django import forms
from django.db.models import fields
from .models import Libros

#Creamos la clase libroform para crear los formularios con los que vamos a trabajar
class LibrosForm (forms.ModelForm):
    
        # La clase meta para la estructura del formulario
    class Meta:
        model = Libros
        fields = '__all__'
