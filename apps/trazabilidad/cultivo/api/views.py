from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.cultivo.models import Cultivo
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.trazabilidad.cultivo.api.serializers import LeerCultivoSerializer, EscribirCultivoSerializer

class CultivoViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticatedOrReadOnly]
    queryset = Cultivo.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return LeerCultivoSerializer
        return EscribirCultivoSerializer