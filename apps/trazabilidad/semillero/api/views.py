from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.trazabilidad.semillero.models import Semillero
from apps.trazabilidad.semillero.api.serializers import LeerSemilleroSerializer, EscribirSemilleroSerializer

class SemilleroModelViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticatedOrReadOnly]
    queryset = Semillero.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LeerSemilleroSerializer
        return EscribirSemilleroSerializer
