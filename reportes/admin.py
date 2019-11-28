from django.contrib import admin
from .models import ControlAsistencia, ControlMaterial

#Código de caso de uso relacionado: C14
admin.site.register(ControlAsistencia)

#Código de caso de uso relacionado: C15
admin.site.register(ControlMaterial)