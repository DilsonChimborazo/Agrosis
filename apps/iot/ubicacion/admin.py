from django.contrib import admin
from apps.iot.ubicacion.models import Ubicacion 

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('latitud','longitud') 
