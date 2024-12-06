from django.contrib import admin
from apps.trazabilidad.semillero.models import Semillero 

@admin.register(Semillero)
class SemilleroAdmin(admin.ModelAdmin):
    list_display = ('nombre_semillero','fecha_siembra','fecha_estimada','cantidad') 
