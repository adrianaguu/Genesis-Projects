from django.contrib import admin
from .models import Inscripcion

"""Peronalizar la página admin de Inscripcion"""
class ActividadesInLine(admin.TabularInline):
    model = Inscripcion.actividades.through
    verbose_name = "Actividad"
    verbose_name_plural = "Actividades"

class InscripcionAdmin(admin.ModelAdmin):
    inlines = [
            ActividadesInLine,
        ]

#Código de caso de uso relacionado: C13
admin.site.register(Inscripcion, InscripcionAdmin)