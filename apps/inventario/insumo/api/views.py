from rest_framework.viewsets import ModelViewSet
from apps.inventario.insumo.models import Insumo
from apps.inventario.insumo.api.serializers import InsumoSereializer

class insumoViewset (ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSereializer 