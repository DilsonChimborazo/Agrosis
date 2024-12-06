from django.db import models

class Rol(models.Model):
    rol = models.CharField(max_length=20, unique=True)
    actualizacion = models.CharField(max_length=50)
    fecha_creacion = models.DateField()

    def __str__(self):
        return self.rol