from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    nombre_insumo = models.CharField(max_length=100)
    precio_unidad = models.DecimalField(max_digits=15, decimal_places=3)
    tipo =models.CharField(max_length=50,choices=tipo_insumo)
    cantidad = models.IntegerField()
    Unidad_Medida=models.CharField(max_length=50,choices=unidad_medida)
    
    def __str__(self):
          return self.nombre_insumo
      
      
class Herramientas(models.Model):
        Tipos_Herramienta=[
            ('Manual','Manual'),
            ('Electrica','ELectrica'),
        ]

        Estados_Herramienta=[
            ('Bueno','Bueno'),
            ('Regular','Regular'),
            ('Malo','Malo'),
        ]

        Estados_Entrega=[
            ('Incompleto','Incompleto'),
            ('Completo','Completo'),
        ]

        nombre = models.CharField(max_length=100)
        estado = models.CharField(max_length=50,choices=Estados_Herramienta)
        fecha_prestamo=models.DateField(null=True, blank=True)
        estado=models.CharField(max_length=50,choices=Estados_Entrega,default='Incompleto')
        
        def __str__(self):
          return self.Tipos_Herramienta


class Requiere(models.Model):
        fk_id_herramientas = models.ForeignKey(Herramientas, on_delete=models.CASCADE) 
        fk_id_asignacion_actividades =models.ForeignKey(asignacion_actividades, on_delete=models.CASCADE) 
        
        def __str__(self):
          return self.f"Requiere
      
      
class 