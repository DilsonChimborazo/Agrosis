from django.contrib import admin
from apps.iot.eras.models import Eras 

@admin.register(Eras)
class ErasAdmin(admin.ModelAdmin):
    list_display = ('descripcion','fk_id_lote') 
