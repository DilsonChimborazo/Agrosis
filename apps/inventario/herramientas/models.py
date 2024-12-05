from django.db import models

# Create your models here.
class Herramientas (models.Model):
    estado = {
        ('Disponible', 'Disponible'),
        ('Prestado', 'Prestado'),
        ('En reparación', 'En reparación')
    }
    nombre_h = models.CharField(max_length=500)
    fecha_prestamo = models.DateTimeField(max_length=200)
    estado = models.CharField(max_length=50 ,choices=estado, null=True)

    def __str__(self):
        return self.nombre_h  