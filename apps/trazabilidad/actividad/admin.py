from django.contrib import admin
from apps.trazabilidad.actividad.models import Actividad

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre_actividad', 'descripcion') 
