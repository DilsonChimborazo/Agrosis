from django.db import models
from apps.plantacion.models import *

class Insumos(models.Model):
    unidad_medida=[
        ('Gramo(gr)','Gramo(gr)'),
        ('Libra(lb)','Libra(lb)'),
        ('Kilogramo(Kg)','Kilogramo(Kg)'),
        ('Quintal(Qn)','Quintal(Qn)'),
        ('Tonelada(Tn)','Tonelada(Tn)'),
        ('Mililitro(Ml)','Mililitro(Ml)'),
        ('Centrilitro(Cn)','Centrilitro(Cn)'),
        ('Decalitro(Dc)','Decalitro(Dc)'),
        ('Litro(L)','Litro(L)'),

    ]

    tipo_insumo=[
        ('Abono','Abono'),
        ('Plaguicida','Plaguicida'),
        ('Quimico','Quimico'),
        ('Semilla','Semilla'),
    ]
#models.DecimalField(max_digits=15, decimal_places=3)
#models.CharField(max_length=100)
    nombre= models.CharField(max_length=100)
    tipo =models.CharField(max_length=50,choices=tipo_insumo)
    precio_unidad = models.DecimalField(max_digits=15, decimal_places=3)
    cantidad = models.IntegerField()
    Unidad_Medida=models.CharField(max_length=50,choices=unidad_medida)
    
    def __str__(self):
        return self.nombre
    
class Herramientas(models.Model):
        Estados_Herramienta=[
            ('Bueno','Bueno'),
            ('Regular','Regular'),
            ('Malo','Malo'),
        ]

        nombre_h = models.CharField(max_length=100)
        fecha_prestamo=models.DateField(null=True, blank=True)
        estado = models.CharField(max_length=50,choices=Estados_Herramienta)
        
        def __str__(self):
            return self.nombre_h


class Requiere(models.Model):
        fk_id_herramientas = models.ForeignKey(Herramientas, on_delete=models.SET_NULL , null=True) 
        fk_id_asignacion_actividades =models.ForeignKey(AsignacionActividades, on_delete=models.SET_NULL , null=True) 
        
        def __str__(self):
            return self.fk_id_herramientas.nombre_h
        
class Utiliza(models.Model):
        fk_id_insumo = models.ForeignKey(Insumos, on_delete=models.SET_NULL , null=True) 
        fk_id_asignacion_actividades =models.ForeignKey(AsignacionActividades, on_delete=models.SET_NULL , null=True) 
        
        def __str__(self):
            return self.fk_id_insumo.nombre

class ControlUsoInsumo(models.Model):
    fk_id_insumo = models.ForeignKey(Insumos, on_delete=models.SET_NULL, null=True) 
    fk_id_control_fitosanitario = models.ForeignKey(Control_fitosanitario, on_delete=models.SET_NULL, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self): return f'{self.fk_id_insumo} - {self.cantidad}'