from django.db import models
from evento.models import Evento
from actividad.models import Actividad

# Create your models here.
class Inscripcion(models.Model):
    """Clase entidad donde se definen los atributos de la tabla Colaborador"""
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=150)
    actividades = models.ManyToManyField(Actividad)
    correo = models.EmailField(max_length=60)
    DNI = models.CharField(max_length=8)
    monto = models.IntegerField(null=True,blank=True)

    """Un objeto de esta clase se muestra por su nombre"""
    def __str__(self):
        return (self.nombre + " " + self.apellido + ' - ' + self.evento.nombre)

    class Meta:
        verbose_name_plural = "Inscripciones"