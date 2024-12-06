from django.contrib import admin
from apps.trazabilidad.realiza.models import Realiza 

@admin.register(Realiza)
class RealizaAdmin(admin.ModelAdmin):
    list_display = ('fk_id_cultivo','fk_id_actividad') 
