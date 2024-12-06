from rest_framework.viewsets import ModelViewSet
from apps.inventario.herramientas.models import Herramientas
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.inventario.herramientas.api.serializers import HerramientasSerializer

class herramientasViewset (ModelViewSet):
    queryset = Herramientas.objects.all()
    permissions_clases = [IsAuthenticatedOrReadOnly]
    serializer_class = HerramientasSerializer 