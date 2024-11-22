from django.db import models
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
    

