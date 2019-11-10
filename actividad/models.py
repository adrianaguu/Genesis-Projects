from django.db import models
from django.utils import timezone
from lugar.models import Ambiente

"""Clase entidad donde se definen los atributos de la tabla Actividad"""
class Actividad(models.Model):
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    hora = models.TimeField()
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    costo_inscripcion=models.FloatField()
    num_incritos=models.IntegerField(blank=True, null=True)


    """Un objeto de esta clase se muestra por su nombre"""
    def __str__(self):
        return self.nombre