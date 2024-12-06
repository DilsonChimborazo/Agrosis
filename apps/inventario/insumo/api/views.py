from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.inventario.insumo.models import Insumo
from apps.inventario.insumo.api.serializers import InsumoSerializer

class insumoViewset (ModelViewSet):
    queryset = Insumo.objects.all()
    permissions_clases = [IsAuthenticated]
    serializer_class = InsumoSerializer 