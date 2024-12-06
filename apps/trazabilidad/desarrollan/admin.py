from django.contrib import admin
from apps.trazabilidad.desarrollan.models import Desarrollan 

@admin.register(Desarrollan)
class DesarrollanAdmin(admin.ModelAdmin):
    list_display = ('fk_id_cultivo','fk_id_pea') 
