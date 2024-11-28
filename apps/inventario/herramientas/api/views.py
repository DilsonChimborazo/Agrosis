from rest_framework.viewsets import ModelViewSet
from apps.inventario.herramientas.models import Herramientas
from apps.inventario.herramientas.api.serializers import HerramientasSereializer

class herramientasViewset (ModelViewSet):
    queryset = Herramientas.objects.all()
    serializer_class = HerramientasSereializer 