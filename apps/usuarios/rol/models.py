from django.db import models

class Rol(models.Model):
    opciones = [
        ('aprendiz', 'Aprendiz'),
        ('pasante', 'Pasante'),
        ('instructor', 'Instructor'),
        ('administrador', 'Administrador')
    ]
    rol = models.CharField(max_length=20, choices=opciones)
    actualizacion = models.CharField(max_length=50)
    fecha_creacion = models.DateField()

    def __str__(self):
        return self.rol