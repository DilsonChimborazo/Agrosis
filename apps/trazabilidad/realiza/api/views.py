from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAutenticated
from apps.trazabilidad.realiza.models import Realiza
from apps.trazabilidad.realiza.api.serializers import LeerRealizaSerializer, EscribirRealizaSerializer

class RealizaModelViewSet(ModelViewSet):
    permissions_clases = [IsAutenticated]
    queryset = Realiza.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LeerRealizaSerializer
        return EscribirRealizaSerializer
