from django.db import models
from apps.trazabilidad.cultivo.models import Cultivo
from apps.trazabilidad.pea.models import Pea

# Create your models here.

class Desarrollan(models.Model):
    fk_id_cultivo = models.ForeignKey(Cultivo, on_delete=models.SET_NULL, null=True)
    fk_id_pea = models.ForeignKey(Pea, on_delete=models.SET_NULL, null=True)  
    def __str__(self): 
        return f"cultivo: {self.fk_id_cultivo.nombre_cultivo} Pea: {self.fk_id_pea.nombre_pea}"  
