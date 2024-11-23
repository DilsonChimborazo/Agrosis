from django.db import models
from apps.plantacion.models import *


# Create your models here.
class Produccion(models.Model):
    cantidad_producida = models.IntegerField()
    fecha=models.DateField(null=True, blank=True)
    
    def __str__(self): 
        return self.cantidad_producida

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)  
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)  
    cantidad = models.IntegerField()  
    fecha = models.DateField()  
    fk_id_produccion = models.ForeignKey(Produccion, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return f"Venta {self.id_venta} - {self.fecha}"
    

class Genera(models.Model):
    fk_id_cultivo = models.ForeignKey(Cultivo, on_delete=models.SET_NULL, null=True) 
    fk_id_produccion = models.ForeignKey(Produccion, on_delete=models.SET_NULL, null=True)
    
    def __str__(self): return self.fk_id_cultivo


