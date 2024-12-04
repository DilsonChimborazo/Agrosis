from django.db import models

# Create your models here.
class Utiliza (models.Model):
    fk_id_insumo = models.ForeignKey ('Insumo', on_delete=models.SET_NULL, null=True)
    fk_id_asignacion_actividades = models.ForeignKey ('AsignacionActividades', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Utiliza: {self.fk_id_insumo} - Utiliza: {self.fk_id_asignaciona_actividades}"