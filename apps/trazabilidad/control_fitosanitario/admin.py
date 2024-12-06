from django.contrib import admin
from apps.trazabilidad.control_fitosanitario.models import Control_fitosanitario 

@admin.register(Control_fitosanitario)
class Control_fitosanitarioAdmin(admin.ModelAdmin):
    list_display = ('fecha_control', 'descripcion','fk_id_desarrollan') 
