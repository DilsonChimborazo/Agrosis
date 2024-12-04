from django.db import models

# Create your models here.

class Pea(models.Model):
    nombre_pea = models.CharField(max_length=100)
    descripcion = models.TextField() 
    def __str__(self): return self.nombre_pea
