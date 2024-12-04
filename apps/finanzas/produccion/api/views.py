from rest_framework.viewsets import ModelViewSet
from apps.finanzas.produccion.models import Produccion
from rest_framework.permissions import IsAutenticated
from apps.finanzas.produccion.api.serializer import ProduccionSerializer

class ProduccionViewSet(ModelViewSet):
    permissions_clases = [IsAutenticated]
    
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer