from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.iot.sensores.models import Sensores
from apps.iot.sensores.api.serializers import SensoresSerializer

class SensoresViewSet(ModelViewSet):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
