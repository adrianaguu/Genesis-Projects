from django.contrib import admin
from .models import Evento, EventoTipo
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(EventoTipo)

class EventoAdmin(admin.ModelAdmin):
    save_as = True
#admin.site.unregister(Group)
# Register your models here.
admin.site.register(Evento, EventoAdmin)