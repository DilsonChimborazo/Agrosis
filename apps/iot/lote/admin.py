from django.contrib import admin
from apps.iot.lote.models import Lote 

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ('estado','fk_id_ubicacion','dimencion','nombre_lote') 
