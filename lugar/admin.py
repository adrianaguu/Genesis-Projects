from django.contrib import admin
from .models import Lugar, Ambiente

# Registra el modelo Lugar en el admin
admin.site.register(Lugar)
# Personificar el admin, para permitir adaptar un ambiente
class AmbienteAdmin(admin.ModelAdmin):
    save_as = True
admin.site.register(Ambiente, AmbienteAdmin)