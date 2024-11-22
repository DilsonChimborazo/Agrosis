from django.contrib.auth.models import AbstractUser
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

class Usuario(AbstractUser): 
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username', 'nombre', 'apellido'] 
    def __str__(self):
        return f"{self.nombre} {self.apellido}"




