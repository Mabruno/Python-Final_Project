from django.db import models

class Curso(models.Model):
    curso = models.CharField(max_length=40)
    id_curso = models.IntegerField()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

class Entregables(models.Model):
    titulo = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    estado_entregado = models.BooleanField(default=False)
