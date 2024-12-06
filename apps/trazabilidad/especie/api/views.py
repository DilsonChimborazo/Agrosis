from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.trazabilidad.especie.models import Especie
from apps.trazabilidad.especie.api.serializers import LeerEspecieSerializer, EscribirEspecieSerializer

class EspecieModelViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticatedOrReadOnly]
    queryset = Especie.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LeerEspecieSerializer
        return EscribirEspecieSerializer
