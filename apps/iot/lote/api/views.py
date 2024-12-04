from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.iot.lote.models import Lote
from apps.iot.lote.api.serializers import leerLoteSerializer, escribirLoteSerializer

class LoteViewSet(ModelViewSet):
    queryset = Lote.objects.all()
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return leerLoteSerializer
        return escribirLoteSerializer


