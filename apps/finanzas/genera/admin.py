from django.contrib import admin
from apps.finanzas.genera.models import Genera 

@admin.register(Genera)
class GeneraAdmin(admin.ModelAdmin):
    list_display = ('fk_id_cultivo','fk_id_produccion','id_genera') 
    
