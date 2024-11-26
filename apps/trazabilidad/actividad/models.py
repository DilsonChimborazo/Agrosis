from django.db import models

# Create your models here.

class Actividad(models.Model):
    nombre_actividad = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_actividad