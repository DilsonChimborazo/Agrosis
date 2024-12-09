from rest_framework.viewsets import ModelViewSet
from apps.usuarios.usuario.models import Usuarios
from apps.usuarios.usuario.api.serializer import LeerUsuarioSerializer, EscribirUsuarioSerlializer
from rest_framework.permissions import IsAuthenticated

class UsuarioViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Usuarios.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LeerUsuarioSerializer
        return EscribirUsuarioSerlializer