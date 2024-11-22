from rest_framework.viewsets import ModelViewSet
from apps.iot.mide.models import Mide
from apps.iot.mide.api.serializers import MideSerializer

class MideViewSet(ModelViewSet):
    queryset = Mide.objects.all()
    serializer_class = MideSerializer
