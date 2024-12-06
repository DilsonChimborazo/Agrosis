from django.db import models
from apps.finanzas.produccion.models import Produccion
# Create your models here.

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)  
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)  
    cantidad = models.IntegerField()  
    fecha = models.DateField()  
    fk_id_produccion = models.ForeignKey(Produccion, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return f"Venta {self.id_venta} - {self.fecha}"