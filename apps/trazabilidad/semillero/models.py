from django.db import models

# Create your models here.

class Semillero(models.Model):
    nombre_semillero = models.CharField(max_length=100)
    fecha_siembra = models.DateField() 
    fecha_estimada = models.DateField() 
    cantidad = models.IntegerField() 

    def __str__(self): return self.nombre_semillero
    

    