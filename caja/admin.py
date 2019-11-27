from django.contrib import admin
from .models import Salida,Ingreso

# Register your models here.
admin.site.register(Ingreso)
admin.site.register(Salida)