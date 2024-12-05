from django.db import models
from apps.inventario.insumo.models import Insumo
from apps.trazabilidad.control_fitosanitario.models import Control_fitosanitario

# Create your models here.
class ControlUsaInsumo(models.Model):
    fk_id_insumo = models.ForeignKey(Insumo, on_delete=models.SET_NULL, null=True)
    fk_id_control_fitosanitario = models.ForeignKey(Control_fitosanitario , on_delete=models.SET_NULL, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Control: {self.cantidad} - Insumo: {self.fk_id_insumo.nombre}"