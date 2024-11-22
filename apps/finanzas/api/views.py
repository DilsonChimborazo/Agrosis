from rest_framework.viewsets import ModelViewSet
from apps.finanzas.models import Venta
from apps.finanzas.api.serializer import VentaSerializer

class VentaViewSet(ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer