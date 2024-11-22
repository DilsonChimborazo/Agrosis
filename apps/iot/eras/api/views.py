from rest_framework.viewsets import ModelViewSet
from apps.iot.eras.models import Eras
from apps.iot.eras.api.serializers import ErasSerializer

class ErasViewSet(ModelViewSet):
    queryset = Eras.objects.all()
    serializer_class = ErasSerializer

