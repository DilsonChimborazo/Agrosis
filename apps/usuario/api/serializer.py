from rest_framework.serializers import ModelSerializer
from apps.usuario.models import Rol, Usuario

class RolSerializer(ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
