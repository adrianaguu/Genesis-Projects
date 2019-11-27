from django.db import models
from evento.models import Evento
from inscripcion.models import Inscripcion
from django.dispatch import receiver
from actividad.models import Actividad
from django.db.models.signals import post_save
from material.models import Material

class ControlAsistencia(models.Model):
    evento = models.OneToOneField(Evento,on_delete=models.CASCADE)
    asistentes = models.ManyToManyField(Inscripcion,blank=True)

    def __str__(self):
        return self.evento.nombre

    class Meta:
        verbose_name_plural = 'Control de Asistencias'

class ControlMaterial(models.Model):
    actividad = models.OneToOneField(Actividad,on_delete=models.CASCADE)
    materiales = models.ManyToManyField(Material,blank=True)

    def __str__(self):
        return self.actividad.nombre

    class Meta:
        verbose_name_plural = 'Control de Materiales'
        


"""Método que registra un ControlAsistencia automaticamente cuando un evento es registrado"""
@receiver(post_save, sender=Evento)
def create_evento_controlasistencia(sender, instance, created, **kwargs):
    if created:
        ControlAsistencia.objects.create(evento=instance)

"""Método que registra un ControlMaterial automaticamente cuando una actividad es registrado"""
@receiver(post_save, sender=Actividad)
def create_actividad_controlmaterial(sender, instance, created, **kwargs):
    if created:
        ControlMaterial.objects.create(actividad=instance)