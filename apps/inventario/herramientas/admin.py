from django.contrib import admin
from apps.inventario.herramientas.models import Herramientas 

@admin.register(Herramientas)
class HerramientasAdmin(admin.ModelAdmin):
    list_display = ('nombre_h','fecha_prestamo','estado') 
    
