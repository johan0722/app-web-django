from django.db import models

# En esta clase libros, inicializamos y creamos los datos con los cuales vamos a trabajar
# En la base de datos

class Libros(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen',null=True)
    descripcion = models.TextField(null = True, verbose_name='Descripcion')


    def __str__(self):
        fila =  "Titulo " + self.titulo + "-" +"Descripcion" + self.descripcion
        return fila

    # Esta funcion, nos ayuda a eliminar una imagen del todo, desde el storage dependiendo el nombre
    def delete(self, using = None, keep_parents= False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
