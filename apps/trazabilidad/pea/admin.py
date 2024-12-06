from django.contrib import admin
from apps.trazabilidad.pea.models import Pea 

@admin.register(Pea)
class PeaAdmin(admin.ModelAdmin):
    list_display = ('nombre_pea', 'descripcion') 
