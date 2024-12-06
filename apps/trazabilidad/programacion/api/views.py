from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.trazabilidad.programacion.models import Programacion
from apps.trazabilidad.programacion.api.serializers import LeerProgramacionSerializer, EscribirProgramacionSerializer

class ProgramacionModelViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticatedOrReadOnly]
    queryset = Programacion.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LeerProgramacionSerializer
        return EscribirProgramacionSerializer
