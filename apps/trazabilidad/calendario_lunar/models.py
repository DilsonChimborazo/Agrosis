from django.db import models

# Create your models here.
class Calendario_lunar(models.Model):
    fecha = models.DateField()
    descripcion_evento = models.TextField()
    evento = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.evento} - {self.fecha}'
