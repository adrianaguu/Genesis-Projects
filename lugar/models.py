from django.db import models
class Lugar(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    def __str__(self):
        return self.nombre
# Create your models here.
