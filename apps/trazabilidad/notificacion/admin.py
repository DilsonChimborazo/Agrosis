from django.contrib import admin
from apps.trazabilidad.notificacion.models import Notificacion 

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'mensaje','fk_id_programacion') 
