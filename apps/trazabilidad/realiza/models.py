from django.db import models
from apps.trazabilidad.cultivo.models import Cultivo
from apps.trazabilidad.actividad.models import Actividad
# Create your models here.
class Realiza(models.Model):
    fk_id_cultivo = models.ForeignKey(Cultivo, on_delete=models.SET_NULL, null=True)
    fk_id_actividad = models.ForeignKey(Actividad, on_delete=models.SET_NULL, null=True) 
    
    def __str__(self):
        return f'{self.fk_id_cultivo}{self.fk_id_actividad}'
