from django.contrib import admin
from apps.trazabilidad.tipo_residuos.models import Tipo_residuos 

@admin.register(Tipo_residuos)
class Tipo_residuosAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo_residuo','descripcion') 
