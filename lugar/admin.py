from django.contrib import admin
from .models import Lugar, Ambiente

admin.site.register(Lugar)
# Register your models here.
class AmbienteAdmin(admin.ModelAdmin):
    save_as = True
admin.site.register(Ambiente, AmbienteAdmin)