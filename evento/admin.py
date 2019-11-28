from django.contrib import admin
from .models import Evento, EventoTipo, Descuento
from django.contrib.auth.models import Group
from actividad.models import Actividad
from lugar.models import Lugar,Ambiente
from colaborador.models import Comite, Colaborador
from inscripcion.models import Inscripcion


#Clase para que aparesca en la página admi del modelo padre
class EventoInline(admin.TabularInline):
    model = Evento

class InscripcionInline(admin.TabularInline):
    model = Inscripcion

class ComiteInLine(admin.TabularInline):
    model = Comite

class ActividadInLine(admin.TabularInline):
    model = Actividad



# Quita el modelo Group en la página admin
admin.site.unregister(Group)

#Clase que personliza el admin del modelo Tipo Evento
class EventoTipoAdmin(admin.ModelAdmin):
    inlines = [
            EventoInline,
        ]



#Clase que personliza el admin del modelo Evento

class EventoAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [
            ActividadInLine,
            ComiteInLine,
            InscripcionInline,
        ]
    ist_display = ('nombre','fecha_inicio','fecha_fin')


    

# Register el modelo evento en la página admin
#Códigos de casos de uso relacionado: C06-01,C06-02,C06-03,C06-04
admin.site.register(Evento, EventoAdmin)
# Registra el modelo Evento Tipo en la página admin
#Códigos de casos de uso relacionado: C05-01,C05-02,C05-03
admin.site.register(EventoTipo, EventoTipoAdmin)
#Códigos de caso de uso relacionado: C13
admin.site.register(Descuento)
