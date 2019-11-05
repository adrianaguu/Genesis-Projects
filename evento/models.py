from django.db import models
from django.utils import timezone
from lugar.models import Lugar

class EventoTipo(models.Model):
    save_as = True
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre

class Evento(models.Model):
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    tipo = models.ForeignKey(EventoTipo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creado = models.DateTimeField(
            default=timezone.now)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.nombre


# Create your models here.
