from rest_framework.viewsets import ModelViewSet
from apps.finanzas.produccion.models import Produccion
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.finanzas.produccion.api.serializers import ProduccionSerializer

class ProduccionViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticatedOrReadOnly]
    
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer