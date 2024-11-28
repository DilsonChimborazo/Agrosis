from django.db import models
from apps.trazabilidad.tipo_cultivo.models import Tipo_cultivo  # Importa el modelo Tipo_cultivo

# Crear tu modelo aquí
class Especie(models.Model):
    nombre_comun = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=100)
    descripcion = models.TextField()
    fk_id_tipo_cultivo = models.ForeignKey(Tipo_cultivo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre_comun
