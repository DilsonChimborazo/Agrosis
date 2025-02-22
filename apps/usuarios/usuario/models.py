from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from apps.usuarios.rol.models import Rol
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("El superusuario debe tener is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class Usuarios(AbstractUser):
 
    fk_id_rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(unique=True) 

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username', 'nombre', 'apellido']  

    objects = UsuarioManager()  

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



