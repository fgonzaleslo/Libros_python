from django.db import models

# Creación de modelos.
#Creación Libros
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    descripcion = models.TextField(verbose_name='Descripcion', null=True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.descripcion
        return fila 
#Creación Autores
class Autor(models.Model):
    id = models.AutoField(primary_key= True)
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos')
    dni = models.IntegerField(max_length=8, verbose_name='DNI')
    direccion = models.TextField(verbose_name='Direccion', null=True)
    libro_id = models.OneToOneField(Libro, on_delete= models.CASCADE)

