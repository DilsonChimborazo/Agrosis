from django.db import models

# Create your models here.

class Produccion(models.Model):
    id_produccion = models.AutoField(primary_key=True)  
    cantidad_produccion = models.DecimalField(null=True,max_digits=20,decimal_places=10)
    fecha = models.DateField() 

    def __str__(self):
        return f"Producción {self.id_produccion} - {self.cantidad_produccion} en {self.fecha}"