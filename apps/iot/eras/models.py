from django.db import models
from apps.iot.lote.models import Lote
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

class Eras(models.Model):
    descripcion = models.TextField()
    fk_id_lote = models.ForeignKey(Lote, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.fk_id_lote.id if self.fk_id_lote else 'Sin Lote'} - {self.descripcion}"

@receiver(post_save, sender=Eras)
def enviar_datos_eras(sender, instance, **kwargs):
    """Envía datos actualizados de Eras al grupo WebSocket 'eras'"""
    channel_layer = get_channel_layer()
    
    data = {
        "id": instance.id,
        "descripcion": instance.descripcion,
        "fk_id_lote": instance.fk_id_lote.id if instance.fk_id_lote else None
    }

    async_to_sync(channel_layer.group_send)(
        "eras",
        {
            "type": "eras_data",
            "message": data
        }
    )
