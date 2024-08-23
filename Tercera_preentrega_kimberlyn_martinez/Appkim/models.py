from django.db import models
from django.db import models

# Crear tus modelos aquí



class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='estudiantes')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    

    def __str__(self):
        return f"Prof. {self.nombre} {self.apellido}"




