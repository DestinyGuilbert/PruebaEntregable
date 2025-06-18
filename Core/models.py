from django.db import models

class Curso (models.Model):
    nombre = models.CharField(max_length=9)
    camada = models.IntegerField()
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=9)
    Apellido = models.CharField(max_length=18)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=9)
    Apellido = models.CharField(max_length=18)
    email = models.EmailField()

class Entregable(models.Model):
    nombre = models.CharField(max_length=9)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()
    
# Create your models here.
