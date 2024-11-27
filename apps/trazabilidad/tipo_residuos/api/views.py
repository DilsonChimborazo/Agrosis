from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.tipo_residuos.models import Tipo_residuos
from apps.trazabilidad.tipo_residuos.api.serializers import Tipo_residuosSerializer

class Tipo_residuosViewSet(ModelViewSet):
    queryset = Tipo_residuos.objects.all()
    serializer_class = Tipo_residuosSerializer