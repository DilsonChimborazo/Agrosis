from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAutenticated
from apps.inventario.insumo.models import Insumo
from apps.inventario.insumo.api.serializers import InsumoSereializer

class insumoViewset (ModelViewSet):
    queryset = Insumo.objects.all()
    permissions_clases = [IsAutenticated]
    serializer_class = InsumoSereializer 