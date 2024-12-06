from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.pea.models import Pea
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.trazabilidad.pea.api.serializers import LeerPeaSerializer

class PeaViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticatedOrReadOnly]
    queryset = Pea.objects.all()
    serializer_class = LeerPeaSerializer