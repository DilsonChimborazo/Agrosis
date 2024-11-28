from django.db import models
from apps.trazabilidad.desarrollan.models import Desarrollan


# Create your models here.
class Control_fitosanitario(models.Model):
    fecha_control = models.DateField()
    descripcion = models.CharField(max_length=300)
    fk_id_desarrollan = models.ForeignKey(Desarrollan, on_delete=models.SET_NULL, null=True)  
    def __str__(self):
        return self.fecha_control 
    