from rest_framework.viewsets import ModelViewSet
from apps.usuario.models import Rol, Usuario
from apps.usuario.api.serializer import RolSerializer, UsuarioSerializer
from apps.usuario.api.permissions import IsUsuarioReadOnly
class RolViewSet(ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(ModelViewSet):
    permission_classes = [IsUsuarioReadOnly]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer