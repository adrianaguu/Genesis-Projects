from django.contrib import admin
from .models import Lugar, Ambiente
from actividad.models import Actividad

# Registra el modelo Lugar en el admin
#admin.site.register(Lugar)
class AmbienteInLine(admin.TabularInline):
    model = Ambiente

class ActividadInLine(admin.TabularInline):
    model = Actividad
# Registra los modelos Actividad en la página admin
#admin.site.register(Actividad)
class LugarAdmin(admin.ModelAdmin):
    inlines = [
            AmbienteInLine
        ]
class AmbienteAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [
            ActividadInLine
        ]    

# Register el modelo evento 
admin.site.register(Lugar, LugarAdmin)
# Personificar el admin, para permitir adaptar un ambiente

admin.site.register(Ambiente, AmbienteAdmin)