from django.contrib import admin
from apps.inventario.requiere.models import Requiere 

@admin.register(Requiere)
class RequiereAdmin(admin.ModelAdmin):
    list_display = ('fk_Id_herramientas','fk_id_asignaciona_actividades') 
    
