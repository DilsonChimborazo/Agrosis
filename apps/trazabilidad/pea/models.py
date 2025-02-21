from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
import json

# Create your models here.

class Pea(models.Model):
    nombre_pea = models.CharField(max_length=100)
    descripcion = models.TextField() 
    
    def __str__(self): return self.nombre_pea
    
@receiver(post_save, sender=Pea)
def enviar_datos_Pea(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    data = {
        "nombre_pea": instance.nombre_pea,
        "descripcion": instance.descripcion,
    }
    async def send_data():
        await channel_layer.group_send(
            "pae",
            {
                "type": "pea_data",
                "message": data
            }
        )
    
    import asyncio
    asyncio.run(send_data())    
