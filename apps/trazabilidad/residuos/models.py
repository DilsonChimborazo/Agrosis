from django.db import models
from apps.trazabilidad.cultivo.models import Cultivo
from apps.trazabilidad.tipo_residuos.models import Tipo_residuos


# Create your models here.

class Residuos(models.Model):
    nombre_residuo = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=300)
    fk_id_cultivo = models.ForeignKey(Cultivo, on_delete=models.SET_NULL, null=True)
    fk_id_tipo_residuo = models.ForeignKey(Tipo_residuos, on_delete=models.SET_NULL, null=True)
    def __str__(self): 
        return f"Cultivo: {self.fk_id_cultivo.nombre_cultivo} residuo: {self.fk_id_tipo_residuo}" 