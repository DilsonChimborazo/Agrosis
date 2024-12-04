from django.db import models

# Create your models here.
class Insumo (models.Model):
    nombre =  models.CharField(max_length=500)
    tipo = models.CharField(max_length=200)
    precio_unidad = models.DecimalField (max_digits=10, decimal_places=2)
    cantidad = models.IntegerField ()
    unidad_medida = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 