from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.iot.ubicacion.models import Ubicacion
from apps.iot.ubicacion.api.serializers import UbicacionSerializer

class UbicacionViewSet(ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

