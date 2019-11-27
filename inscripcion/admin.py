from django.contrib import admin
from .models import Inscripcion


class ActividadesInLine(admin.TabularInline):
    model = Inscripcion.actividades.through
    verbose_name = "Actividad"
    verbose_name_plural = "Actividades"

# Register your models here.
class InscripcionAdmin(admin.ModelAdmin):
    inlines = [
            ActividadesInLine,
        ]

admin.site.register(Inscripcion, InscripcionAdmin)