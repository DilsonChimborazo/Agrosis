from django.db import models

# Create your models here.
class ControlUsaInsumo(models.Model):
    fk_id_insumo = models.ForeignKey(Insumo, on_delete=models.SET_NULL, null=True)
    fk_id_control_fitosanitario = models.ForeignKey('ControlFitosanitario', on_delete=models.SET_NULL, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Control: {self.id_control_usa_insumo} - Insumo: {self.fk_id_insumo.nombre}"