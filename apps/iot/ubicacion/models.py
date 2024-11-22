from django.db import models

# Create your models here.
class Ubicacion(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return self.latitud, self.longitud