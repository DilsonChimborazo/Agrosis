from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.cultivo.models import Cultivo
from apps.trazabilidad.cultivo.api.serializers import LeerCultivoSerializer, EscribirCultivoSerializer

class CultivoViewSet(ModelViewSet):
    queryset = Cultivo.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return LeerCultivoSerializer
        return EscribirCultivoSerializer