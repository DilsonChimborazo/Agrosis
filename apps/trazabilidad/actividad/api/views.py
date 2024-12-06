from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.actividad.models import Actividad
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.trazabilidad.actividad.api.serializers import LeerActividadSerializer

class ActividadViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticatedOrReadOnly]
    queryset = Actividad.objects.all()
    serializer_class = LeerActividadSerializer