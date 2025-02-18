from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
import json
# Create your models here.
class Sensores(models.Model):
    nombre_sensor = models.CharField(max_length=50)
    tipo_sensor = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=50)
    descripcion = models.TextField()
    medida_minima = models.IntegerField()
    medida_maxima = models.IntegerField()

    def __str__(self):
        return self.nombre_sensor

@receiver(post_save, sender=Sensores)
def enviar_datos_sensores(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    data = {
        "nombre_sensor": instance.nombre_sensor,
        "tipo_sensor": instance.tipo_sensor,
        "unidad_medida": instance.unidad_medida,
        "descripcion": instance.descripcion,
        "medida_minima": instance.medida_minima,
        "medida_maxima": instance.medida_maxima,
    }
    async def send_data():
        await channel_layer.group_send(
            "sensores",
            {
                "type": "sensor_data",
                "message": data
            }
        )
    
    import asyncio
    asyncio.run(send_data())

