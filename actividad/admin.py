from django.contrib import admin
from .models import Actividad
from material.models import Material

class MaterialInLine(admin.TabularInline):
    model = Material
# Registra los modelos Actividad en la página admin
#admin.site.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [
            MaterialInLine
        ]
    

# Casos de uso relacionados: C07-01,C07-02,C07-03
admin.site.register(Actividad, ActividadAdmin)
