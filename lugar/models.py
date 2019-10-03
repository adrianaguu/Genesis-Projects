from django.db import models
class Lugar(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    def __str__(self):
        return self.nombre


class Ambiente(models.Model):
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    identificador = models.CharField(max_length=200, unique=True)
    ubicación = models.CharField(max_length=500)
    capacidad = models.IntegerField()
    descripcion = models.TextField()
    tipo = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre
