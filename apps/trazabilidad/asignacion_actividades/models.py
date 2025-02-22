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
