from django.contrib import admin
from apps.inventario.utiliza.models import Utiliza 

@admin.register(Utiliza)
class UtilizaAdmin(admin.ModelAdmin):
    list_display = ('fk_id_insumo','fk_id_asignacion_actividades') 
    
