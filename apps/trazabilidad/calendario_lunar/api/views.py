from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.trazabilidad.calendario_lunar.models import Calendario_lunar
from apps.trazabilidad.calendario_lunar.api.serializers import LeerCalendario_lunarSerializer, EscribirCalendario_lunarSerializer

class Calendario_lunarModelViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticatedOrReadOnly]
    queryset = Calendario_lunar.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LeerCalendario_lunarSerializer
        return EscribirCalendario_lunarSerializer
