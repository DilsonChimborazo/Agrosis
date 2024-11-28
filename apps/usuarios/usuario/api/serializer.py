from rest_framework.serializers import ModelSerializer
from apps.usuarios.usuario.models import Usuario
from apps.usuarios.rol.api.serializer import RolSerializer


class LeerUsuarioSerializer(ModelSerializer):
    fk_id_rol = RolSerializer()
    
    class Meta:
        model = Usuario
        fields = '__all__'

class EscribirUsuarioSerlializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
