from django.urls import path
from . import views # Importamos las vistas del proyecto

urlpatterns = [
     path('', views.inicio, name='inicio'),
     path('nosotros', views.nosotros, name='nosotros'),
     path('libros', views.libros, name='libros'),
     path('libros/crear', views.crear, name='crear'),
     path('libros/editar', views.editar, name='editar'),
]
