from rest_framework.viewsets import ModelViewSet
from apps.finanzas.models import *
from apps.finanzas.api.serializer import *

class VentaViewSet(ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class ProduccionViewSet(ModelViewSet):
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer

class GeneraViewSet(ModelViewSet):
    queryset = Genera.objects.all()
    serializer_class = GeneraSerializer