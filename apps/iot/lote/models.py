from django.db import models
from apps.iot.ubicacion.models import Ubicacion

# Create your models here.
class Lote(models.Model):
    estados = [
        ('disponible', 'Disponible'),
        ('ocupado', 'ocupado'),
    ]
    dimencion = models.IntegerField()
    nombre_lote = models.CharField(max_length=500)
    fk_id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=50, choices=estados, null=True)

    def __str__(self):
        return self.nombre_lote