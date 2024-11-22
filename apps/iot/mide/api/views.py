from rest_framework.viewsets import ModelViewSet
from apps.sensores.models import Sensores, Mide
from apps.sensores.api.serializers import SensoresSerializer,MideSerializer

class SensoresViewSet(ModelViewSet):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer

class MideViewSet(ModelViewSet):
    queryset = Mide.objects.all()
    serializer_class = MideSerializer