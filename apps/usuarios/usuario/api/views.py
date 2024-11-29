from rest_framework.viewsets import ModelViewSet
from apps.usuarios.usuario.models import Usuario
from apps.usuarios.usuario.api.serializer import LeerUsuarioSerializer, EscribirUsuarioSerlializer
from apps.usuarios.usuario.api.permissions import IsUsuarioReadOnly
from rest_framework.permissions import IsAuthenticated

class UsuarioViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LeerUsuarioSerializer
        return EscribirUsuarioSerlializer