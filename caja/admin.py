from django.contrib import admin
from .models import Salida,Ingreso

# Casos de uso relacionados: C11-05
admin.site.register(Ingreso)

# Casos de uso relacionados: C11-05
admin.site.register(Salida)