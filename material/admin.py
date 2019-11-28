from django.contrib import admin
from .models import Material

# Registra el modelos Material en la página admin
#Códigos de casos de uso relacionado: C04-01,C04-02,C04-03
admin.site.register(Material)

