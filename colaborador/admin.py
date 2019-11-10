from django.contrib import admin
from .models import Colaborador,Comite

# Registra los modelos Colaborador y Comite en la página admin
admin.site.register(Colaborador)
admin.site.register(Comite)