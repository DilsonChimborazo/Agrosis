from django.contrib import admin
from apps.trazabilidad.tipo_cultivo.models import Tipo_cultivo 

@admin.register(Tipo_cultivo)
class Tipo_cultivoAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion') 
