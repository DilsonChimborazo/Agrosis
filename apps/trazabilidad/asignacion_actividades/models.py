from django.db import models
from apps.trazabilidad.actividad.models import Actividad
from apps.usuarios.usuario.models import Usuarios
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
import json

# Create your models here.
class Asignacion_actividades(models.Model):
    fecha = models.DateField()
    observaciones = models.TextField() 
    fk_id_actividad = models.ForeignKey(Actividad, on_delete=models.SET_NULL, null=True)
    id_identificacion = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True)
    
    def __str__(self): 
        return f'{self.fk_id_actividad} - {self.id_identificacion}'


@receiver(post_save, sender=Asignacion_actividades)
def enviar_datos_asignacion_actividades(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    data = {
        "fecha": instance.fecha,
        "fk_id_actividad": instance.fk_id_actividad,
        "id_identificacion": instance.id_identificacion
        
    }
    async def send_data():
        await channel_layer.group_send(
            "asignacion_actividades",
            {
                "type": "asignacion_actividades_data",
                "message": data
            }
        )
    
    import asyncio
    asyncio.run(send_data())