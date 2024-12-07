from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.usuarios.rol.models import Rol

class Usuarios(AbstractUser): 
    fk_id_rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username', 'nombre', 'apellido'] 
    def __str__(self):
        return f"{self.nombre} {self.apellido}"




