from django.db import models
from apps.trazabilidad.especie.models import Especie
from apps.trazabilidad.semillero.models import Semillero

# Create your models here.
class Cultivo(models.Model):
    nombre_cultivo = models.CharField(max_length=100)
    fecha_plantacion = models.DateField()
    descripcion = models.CharField(max_length=300)
    fk_id_especie = models.ForeignKey(Especie, on_delete=models.SET_NULL, null=True)
    fk_id_semillero = models.ForeignKey(Semillero, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nombre_cultivo
