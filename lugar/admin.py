from django.contrib import admin
from .models import Lugar, Ambiente
from actividad.models import Actividad
from evento.models import Evento

# Registra el modelo Lugar en el admin
#admin.site.register(Lugar)
class EventoInLine(admin.TabularInline):
    model = Evento

class AmbienteInLine(admin.TabularInline):
    model = Ambiente

class ActividadInLine(admin.TabularInline):
    model = Actividad
# Registra los modelos Actividad en la página admin
#admin.site.register(Actividad)
class LugarAdmin(admin.ModelAdmin):
    inlines = [
            AmbienteInLine,
            EventoInLine,
        ]
class AmbienteAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [
            ActividadInLine
        ]    

# Register el modelo Lugar en admin
#Códigos de casos de uso relacionado: C08-01,C08-02,C08-03
admin.site.register(Lugar, LugarAdmin)

# Personalizar el admin, para permitir adaptar un ambiente
#Códigos de casos de uso relacionado: C09-01,C09-02,C09-03,C09-04
admin.site.register(Ambiente, AmbienteAdmin)