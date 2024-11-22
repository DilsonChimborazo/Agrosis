from rest_framework.viewsets import ModelViewSet
from apps.iot.sensores.models import Sensores
from apps.iot.sensores.api.serializers import SensoresSerializer

class SensoresViewSet(ModelViewSet):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
