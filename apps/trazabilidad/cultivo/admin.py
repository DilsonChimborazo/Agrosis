from django.contrib import admin
from apps.trazabilidad.cultivo.models import Cultivo 

@admin.register(Cultivo)
class CultivoAdmin(admin.ModelAdmin):
    list_display = ('nombre_cultivo', 'fecha_plantacion','descripcion','fk_id_especie','fk_id_semillero') 
