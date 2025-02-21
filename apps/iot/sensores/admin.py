from django.contrib import admin
from apps.iot.sensores.models import Sensores 

@admin.register(Sensores)
class SensoresAdmin(admin.ModelAdmin):
    list_display = ('nombre_sensor','tipo_sensor','unidad_medida','descripcion','medida_minima','medida_maxima') 
