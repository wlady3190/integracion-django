from django.db import models

# Create your models here.


class Profesor (models.Model):
    nombre = models.CharField(max_length = 100, verbose_name= 'nombre')
    apellido = models.CharField(max_length = 100, verbose_name= 'apellido')
    materia = models.CharField(max_length = 100, verbose_name= 'materia')
    correo = models.EmailField(verbose_name= 'correo')
    
