from rest_framework.viewsets import ModelViewSet
from apps.inventario.herramientas.models import Herramientas
from rest_framework.permissions import IsAutenticated
from apps.inventario.herramientas.api.serializers import HerramientasSereializer

class herramientasViewset (ModelViewSet):
    queryset = Herramientas.objects.all()
    permissions_clases = [IsAutenticated]
    serializer_class = HerramientasSereializer 