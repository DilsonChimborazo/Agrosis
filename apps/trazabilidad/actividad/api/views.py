from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.actividad.models import Actividad
from apps.trazabilidad.actividad.api.serializers import ActividadSerializer

class ActividadViewSet(ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer