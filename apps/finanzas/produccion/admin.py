from django.contrib import admin
from apps.finanzas.produccion.models import Produccion 

@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = ('id_produccion','cantidad_produccion','fecha') 
    
