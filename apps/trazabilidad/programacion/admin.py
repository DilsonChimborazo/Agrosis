from django.contrib import admin
from apps.trazabilidad.programacion.models import Programacion 

@admin.register(Programacion)
class ProgramacionAdmin(admin.ModelAdmin):
    list_display = ('estado', 'fecha_programada', 'duracion','fk_id_asignacionActividades','fk_id_calendario') 
