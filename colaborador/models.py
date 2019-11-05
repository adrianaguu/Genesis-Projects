from django.db import models
from django.utils import timezone
from actividad.models import Actividad

class Comite(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Colaborador(models.Model):
    comite = models.ForeignKey(Comite, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    DNI = models.CharField(max_length=8)


    def __str__(self):
        return self.nombre
