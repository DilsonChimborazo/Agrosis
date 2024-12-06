from django.contrib import admin
from apps.trazabilidad.residuos.models import Residuos 

@admin.register(Residuos)
class ResiduosAdmin(admin.ModelAdmin):
    list_display = ('nombre_residuo','fecha','descripcion','fk_id_cultivo','fk_id_tipo_residuo') 
