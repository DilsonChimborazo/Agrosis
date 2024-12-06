from django.contrib import admin
from apps.trazabilidad.especie.models import Especie 

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nombre_comun', 'nombre_cientifico','descripcion','fk_id_tipo_cultivo') 
