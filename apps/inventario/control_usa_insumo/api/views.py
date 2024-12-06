from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.inventario.control_usa_insumo.models import ControlUsaInsumo
from apps.inventario.control_usa_insumo.api.serializers import LeerControlUsaInsumoSerializer, ControlUsaInsumoSereializer

class ControlUsaInsumoViewset (ModelViewSet):
    queryset = ControlUsaInsumo.objects.all()
    permissions_clases = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrive']:
            return LeerControlUsaInsumoSerializer
        return ControlUsaInsumoSereializer