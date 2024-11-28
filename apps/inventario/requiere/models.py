from django.db import models

# Create your models here.
class Requiere (models.Model):
    fk_Id_herramientas = models.ForeignKey ('herramientas', on_delete=models.SET_NULL, null=True)
    fk_id_asignaciona_actividades = models.ForeignKey ('AsignacionActividades', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Requiere: {self.fk_Id_herramientas} - Requiere: {self.fk_id_asignaciona_actividades}"