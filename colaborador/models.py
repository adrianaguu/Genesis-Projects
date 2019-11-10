from django.db import models
from django.utils import timezone
from actividad.models import Actividad
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Comite(models.Model):
    """Clase entidad donde se definen los atributos de la tabla Comite"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)

    """Un objeto de esta clase se muestra por su nombre"""
    def __str__(self):
        return self.nombre

class Colaborador(models.Model):
    """Clase entidad donde se definen los atributos de la tabla Colaborador"""
    comite = models.ForeignKey(Comite, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DNI = models.CharField(max_length=8)

    """Un objeto de esta clase se muestra por su nombre"""
    def __str__(self):
        return self.nombre

