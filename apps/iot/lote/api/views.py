from rest_framework.viewsets import ModelViewSet
from apps.iot.lote.models import Lote
from apps.iot.lote.api.serializers import LoteSerializer

class LoteViewSet(ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

