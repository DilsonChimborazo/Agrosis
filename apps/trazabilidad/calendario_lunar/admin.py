from django.contrib import admin
from apps.trazabilidad.calendario_lunar.models import Calendario_lunar 

@admin.register(Calendario_lunar)
class Calendario_lunarAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'descripcion_evento', 'evento') 
