from django.contrib import admin
from .models import Evento, EventoTipo
from django.contrib.auth.models import Group

# Quita el modelo Group en la página admin
admin.site.unregister(Group)
# Registra el modelo Evento Tipo en la página admin
admin.site.register(EventoTipo)

#Clase que personliza el admin del modelo Evento
class EventoAdmin(admin.ModelAdmin):
    save_as = True

# Register el modelo evento 
admin.site.register(Evento, EventoAdmin)