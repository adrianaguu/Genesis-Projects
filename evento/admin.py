from django.contrib import admin
from .models import Evento, EventoTipo
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(EventoTipo)
admin.site.register(Evento)
#admin.site.unregister(Group)
# Register your models here.
