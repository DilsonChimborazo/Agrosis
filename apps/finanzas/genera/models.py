from django.db import models

# Create your models here.

class Genera(models.Model):
    id_genera = models.AutoField(primary_key=True)
    fk_id_cultivo = models.ForeignKey(Cultivo, on_delete=models.SET_NULL)
    fk_id_produccion = models.ForeignKey(Produccion, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.id_genera} - El Cultivo {self.fk_id_cultivo}, generó una producción {self.fk_id_produccion}"