from django.db import models
from apps.trazabilidad.models import Eras
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
    

class Mide(models.Model):
    fk_id_sensor = models.ForeignKey(Sensores, on_delete=models.SET_NULL, null=True)
    fk_id_era = models.ForeignKey(Eras, on_delete=models.SET_NULL , null=True)

    def __str__(self):
        return f"Nombre del sensor: {self.fk_id_sensor.nombre_sensor} Era: {self.fk_id_era}"  

