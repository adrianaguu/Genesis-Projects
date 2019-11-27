from django.db import models
from django.utils import timezone
from lugar.models import Lugar


"""Clase entidad donde se definen los atributos de la tabla Tipo Evento"""
class EventoTipo(models.Model):
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    

    """Un objeto de esta clase se muestra por su nombre"""
    def __str__(self):
        return self.nombre


"""Clase entidad donde se definen los atributos de la tabla Evento"""
class Evento(models.Model):
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    tipo = models.ForeignKey(EventoTipo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creado = models.DateTimeField(
            default=timezone.now)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    imagen = models.ImageField(upload_to='images/',null=True,blank=True)
    
    

    """Un objeto de esta clase se muestra por su identificador"""
    def __str__(self):
        return self.nombre

class Descuento(models.Model):
    porcentaje_descuento=models.FloatField(max_length=4)
    limite_uso=models.IntegerField()
    codigo=models.CharField(max_length=16,unique=True)
    nombre = models.CharField(max_length=200)
    """Un objeto de esta clase se muestra por su nombre"""
    def __str__(self):
        return self.nombre






