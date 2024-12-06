from django.db import models
from apps.iot.lote.models import Lote

# Create your models here.
class Eras(models.Model):
    descripcion = models.TextField()
    fk_id_lote = models.ForeignKey(Lote, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.fk_id_lote