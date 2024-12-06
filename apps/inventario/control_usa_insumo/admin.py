from django.contrib import admin
from apps.inventario.control_usa_insumo.models import ControlUsaInsumo 

@admin.register(ControlUsaInsumo)
class Control_uso_insumoAdmin(admin.ModelAdmin):
    list_display = ('fk_id_insumo','fk_id_control_fitosanitario','cantidad') 
    
