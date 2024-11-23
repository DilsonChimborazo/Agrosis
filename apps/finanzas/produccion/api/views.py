from rest_framework.viewsets import ModelViewSet
from apps.finanzas.produccion.models import Produccion
from apps.finanzas.produccion.api.serializer import ProduccionSerializer

class ProduccionViewSet(ModelViewSet):
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer