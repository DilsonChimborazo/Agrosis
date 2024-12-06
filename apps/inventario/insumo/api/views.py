from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.inventario.insumo.models import Insumo
from apps.inventario.insumo.api.serializers import InsumoSerializer

class insumoViewset (ModelViewSet):
    queryset = Insumo.objects.all()
    permissions_clases = [IsAuthenticatedOrReadOnly]
    serializer_class = InsumoSerializer 