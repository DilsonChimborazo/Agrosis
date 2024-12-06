from django.contrib import admin
from apps.iot.mide.models import Mide 

@admin.register(Mide)
class MideAdmin(admin.ModelAdmin):
    list_display = ('valor_medicion','fecha_medicion','fk_id_sensor','fk_id_era',) 
