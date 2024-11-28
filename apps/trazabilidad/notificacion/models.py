from django.db import models
from apps.trazabilidad.programacion.models import Programacion

# Create your models here.
class Notificacion(models.Model):
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    fk_id_programacion = models.ForeignKey(Programacion, on_delete=models.SET_NULL, null=True) 
    
    def __str__(self): return self.titulo
