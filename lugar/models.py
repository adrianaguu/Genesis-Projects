from django.db import models

"""Clase entidad donde se definen los atributos de la tabla Lugar"""
class Lugar(models.Model):
    save_as = True
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()

    """Un objeto de esta clase se muestra por su nombre"""
    def __str__(self):
        return self.nombre


"""Clase entidad donde se definen los atributos de la tabla Ambiente"""
class Ambiente(models.Model):
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    identificador = models.CharField(max_length=200, unique=True)
    ubicación = models.CharField(max_length=500)
    capacidad = models.IntegerField()
    descripcion = models.TextField()
    tipo = models.CharField(max_length=10)

    """Un objeto de esta clase se muestra por su identificador"""
    def __str__(self):
        return self.identificador
