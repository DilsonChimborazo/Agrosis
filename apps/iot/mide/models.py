from django.db import models
from apps.iot.eras.models import Eras
from apps.iot.sensores.models import Sensores

# Create your models here.
class Mide(models.Model):
    fk_id_sensor = models.ForeignKey(Sensores, on_delete=models.SET_NULL, null=True)
    fk_id_era = models.ForeignKey(Eras, on_delete=models.SET_NULL, null=True)
    valor_medicion =  models.DecimalField(max_digits=10, decimal_places=2) 
    fecha_medicion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nombre del sensor: {self.fk_id_sensor.nombre_sensor} Era: {self.fk_id_era}"  