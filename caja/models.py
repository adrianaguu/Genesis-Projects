from django.db import models
from django.utils import timezone
from evento.models import Evento
from material.models import Material
from inscripcion.models import Inscripcion
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Ingreso(models.Model):
    cantidad = models.FloatField()
    fecha = models.DateTimeField()
    evento = models.ForeignKey(Evento,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cantidad)

class Salida(models.Model):
    cantidad = models.FloatField()
    fecha = models.DateTimeField()
    evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=12,null=True)
    concepto  = models.CharField(max_length=60,null=True)
    def __str__(self):
        return str(self.cantidad)

"""Método que registra un Ingreso autmaticamente cuando una inscripción es registrada"""
@receiver(post_save, sender=Inscripcion)
def create_inscripcion_ingreso(sender, instance, created, **kwargs):
    if created:
        if(instance.monto and instance.monto>0):
            Ingreso.objects.create(evento=instance.evento,cantidad=instance.monto,fecha=timezone.now())
  

"""Método que registra una Salida autmaticamente cuando un material es registrado"""
@receiver(post_save, sender=Material)
def create_material_salida(sender, instance, created, **kwargs):
    if created:
        #Se calcula el monto total segun la cantidad y el precio de unidad del material
        sum = instance.cantidad * instance.precio_unidad
        Salida.objects.create(evento=instance.actividad.evento,cantidad=sum,fecha=timezone.now())