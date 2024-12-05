from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.trazabilidad.tipo_residuos.models import Tipo_residuos
from apps.trazabilidad.tipo_residuos.api.serializers import LeerTipo_residuosSerializer

class Tipo_residuosViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticated]
    queryset = Tipo_residuos.objects.all()
    serializer_class = LeerTipo_residuosSerializer