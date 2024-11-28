from rest_framework.viewsets import ModelViewSet
from apps.usuarios.rol.models import Rol
from apps.usuarios.rol.api.serializer import RolSerializer

class RolViewSet(ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer