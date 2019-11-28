from django.contrib import admin
from .models import Colaborador,Comite
# Registra los modelos Colaborador y Comite en la página admin
# Casos de uso relacionados: C03-01,C03-02,C03-03
admin.site.register(Colaborador)



class ColaboradorInLine(admin.TabularInline):
    model = Colaborador
# Registra los modelos Actividad en la página admin
#admin.site.register(Actividad)
class ComiteAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [
            ColaboradorInLine
        ]
    

# Register el modelo evento 
# Casos de uso relacionados: C02-01,C02-02,C02-03
admin.site.register(Comite, ComiteAdmin)