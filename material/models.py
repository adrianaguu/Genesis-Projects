from django.db import models
from django.utils import timezone
from actividad.models import Actividad


"""Clase entidad donde se definen los atributos de la tabla Material"""
class Material(models.Model):
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=200)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    precio_unidad=models.FloatField()
    cantidad=models.IntegerField(blank=True, null=True)

    """Un objeto de esta clase se muestra por su nombre"""
    def __str__(self):
        return self.nombre
