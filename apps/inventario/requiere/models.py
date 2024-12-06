from django.db import models
from apps.inventario.herramientas.models import Herramientas
from apps.trazabilidad.asignacion_actividades.models import Asignacion_actividades

# Create your models here.
class Requiere(models.Model):
    fk_Id_herramientas = models.ForeignKey(Herramientas, on_delete=models.SET_NULL, null=True)
    fk_id_asignaciona_actividades = models.ForeignKey(Asignacion_actividades, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Requiere: {self.fk_Id_herramientas} - Requiere: {self.fk_id_asignaciona_actividades}"