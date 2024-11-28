from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.especie.models import Especie
from apps.trazabilidad.especie.api.serializers import LeerEspecieSerializer, EscribirEspecieSerializer

class EspecieModelViewSet(ModelViewSet):
    queryset = Especie.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LeerEspecieSerializer
        return EscribirEspecieSerializer
