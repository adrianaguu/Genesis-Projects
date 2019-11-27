from django.contrib import admin
from .models import ControlAsistencia, ControlMaterial

# Register your models here.
admin.site.register(ControlAsistencia)
admin.site.register(ControlMaterial)