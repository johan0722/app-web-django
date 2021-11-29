from django.urls import path
from . import views # Importamos las vistas del proyecto

# Importamos el archivo de configuracion de django
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
     path('', views.inicio, name='inicio'),
     path('nosotros', views.nosotros, name='nosotros'),
     path('libros', views.libros, name='libros'),
     path('libros/crear', views.crear, name='crear'),
     path('libros/editar', views.editar, name='editar'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
