
from django.db import models
from apps.inventario.models import *
from apps.usuario.models import *

# Create your models here.

#p
class TipoCultivo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Especie(models.Model):
    nombre_comun = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=100)
    descripcion = models.TextField()
    fk_id_tipo_cultivo = models.ForeignKey(TipoCultivo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre_comun

class Semillero(models.Model):
    nombre_semillero = models.CharField(max_length=100)
    fecha_siembra = models.DateField() 
    fecha_estimada = models.DateField() 
    cantidad = models.IntegerField() 

    def __str__(self): return self.nombre_semillero
    
    
#x    

class Ubicacion(models.Model):
    latitud = models.IntegerField()
    longitud = models.IntegerField()
    def __str__(self): return self.latitud

class Lote(models.Model):
    opcion = [("disponible","disponible"), ("ocupado","ocupado")]
    dimencion = models.IntegerField() 
    nombre_lote = models.CharField(max_length=100)
    fk_id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=100, choices= opcion, default="disponible")
    def __str__(self): return self.nombre_lote

class Eras(models.Model):
    descripcion = models.CharField(max_length=300)
    fk_id_lote = models.ForeignKey(Lote, on_delete=models.SET_NULL, null=True)  
    def __str__(self): return self.descripcion  

class Cultivo(models.Model):
    nombre_cultivo = models.CharField(max_length=100)
    fecha_plantacion = models.DateField()
    descripcion = models.CharField(max_length=300)
    fk_id_especie = models.ForeignKey(Especie, on_delete=models.SET_NULL, null=True)
    fk_id_semillero = models.ForeignKey(Semillero, on_delete=models.SET_NULL, null=True)
    def __str__(self): return self.nombre_cultivo
        
class Plantacion(models.Model):
    fk_id_eras = models.ForeignKey(Eras, on_delete=models.SET_NULL, null=True)
    fk_id_cultivo = models.ForeignKey(Cultivo, on_delete=models.SET_NULL, null=True)
    def __str__(self): return self.fk_id_eras

class Pea(models.Model):
    nombre_pea = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300) 
    def __str__(self): return self.nombre_pea
    
class Desarrollan(models.Model):
    fk_id_cultivo = models.ForeignKey(Cultivo, on_delete=models.SET_NULL, null=True)
    fk_id_pea = models.ForeignKey(Pea, on_delete=models.SET_NULL, null=True)  
    def __str__(self): return self.fk_id_cultivo
    
class Tipo_residuos(models.Model):
    nombre_tipo_residuo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300) 
    def __str__(self): return self.nombre_tipo_residuo
    
class Residuos(models.Model):
    nombre_residuo = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=300)
    fk_id_cultivo = models.ForeignKey(Cultivo, on_delete=models.SET_NULL, null=True)
    fk_id_tipo_residuo = models.ForeignKey(Tipo_residuos, on_delete=models.SET_NULL, null=True)
    def __str__(self): return self.nombre_residuo
    
class Control_fitosanitario(models.Model):
    fecha_control = models.DateField()
    descripcion = models.CharField(max_length=300)
    fk_id_desarrollan = models.ForeignKey(Desarrollan, on_delete=models.SET_NULL, null=True)  
    def __str__(self): return self.fecha_control 
    
    
    

#p

class Actividad(models.Model):
    nombre_actividad = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_actividad
    
class Realiza(models.Model):
    fk_id_cultivo = models.ForeignKey(Cultivo, on_delete=models.SET_NULL, null=True)
    fk_id_actividad = models.ForeignKey(Actividad, on_delete=models.SET_NULL, null=True) 
    
    def __str__(self):
        return f'{self.fk_id_cultivo}{self.fk_id_actividad}'

class AsignacionActividades(models.Model):
    fecha = models.DateField()
    observaciones = models.TextField() 
    fk_id_actividad = models.ForeignKey(Actividad, on_delete=models.SET_NULL, null=True)
    id_identificacion = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    
    def __str__(self): return f'{self.fk_id_actividad} - {self.id_identificacion}'

class CalendarioLunar(models.Model):
    fecha = models.DateField()
    descripcion_evento = models.TextField()
    evento = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.evento} - {self.fecha}'

class Programacion(models.Model): 
    estado = models.CharField(max_length=50) 
    fecha_programada = models.DateTimeField() 
    duracion = models.DurationField()
    fk_id_asignacionActividades = models.ForeignKey(AsignacionActividades, on_delete=models.SET_NULL, null=True)
    fk_id_calendario = models.ForeignKey(CalendarioLunar, on_delete=models.SET_NULL, null=True) 
    
    def __str__(self): return f'{self.estado} - {self.fecha_programada}'

class Notificacion(models.Model):
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    fk_id_programacion = models.ForeignKey(Programacion, on_delete=models.SET_NULL, null=True) 
    
    def __str__(self): return self.titulo

class ControlUsoInsumo(models.Model):
    fk_id_insumo = models.ForeignKey(Insumos, on_delete=models.SET_NULL, null=True) 
    fk_id_control_fitosanitario = models.ForeignKey(Control_fitosanitario, on_delete=models.SET_NULL, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self): return f'{self.fk_id_insumo} - {self.cantidad}'


