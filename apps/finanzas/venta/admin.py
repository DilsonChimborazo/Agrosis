from django.contrib import admin
from apps.finanzas.venta.models import Venta 

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_venta','fk_id_produccion','precio_unidad','cantidad','fecha') 
    
