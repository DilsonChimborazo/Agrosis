from django.db import models
from apps.trazabilidad.asignacion_actividades.models import Asignacion_actividades
from apps.trazabilidad.calendario_lunar.models import Calendario_lunar

# Create your models here.
class Programacion(models.Model): 
    estado = models.CharField(max_length=50) 
    fecha_programada = models.DateTimeField() 
    duracion = models.DurationField()
    fk_id_asignacionActividades = models.ForeignKey(Asignacion_actividades, on_delete=models.SET_NULL, null=True)
    fk_id_calendario = models.ForeignKey(Calendario_lunar, on_delete=models.SET_NULL, null=True) 
    
    def __str__(self): return f'{self.estado} - {self.fecha_programada}'
