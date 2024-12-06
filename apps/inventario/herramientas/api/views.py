from rest_framework.viewsets import ModelViewSet
from apps.inventario.herramientas.models import Herramientas
from rest_framework.permissions import IsAuthenticated
from apps.inventario.herramientas.api.serializers import HerramientasSerializer

class herramientasViewset (ModelViewSet):
    queryset = Herramientas.objects.all()
    permissions_clases = [IsAuthenticated]
    serializer_class = HerramientasSerializer 