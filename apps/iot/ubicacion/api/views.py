from rest_framework.viewsets import ModelViewSet
from apps.iot.ubicacion.models import Ubicacion
from apps.iot.ubicacion.api.serializers import UbicacionSerializer

class UbicacionViewSet(ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer