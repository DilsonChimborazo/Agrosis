from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.pea.models import Pea
from apps.trazabilidad.pea.api.serializers import LeerPeaSerializer

class PeaViewSet(ModelViewSet):
    queryset = Pea.objects.all()
    serializer_class = LeerPeaSerializer