from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.desarrollan.models import Desarrollan
from rest_framework.permissions import IsAuthenticated
from apps.trazabilidad.desarrollan.api.serializers import LeerDesarrollanSerializer, escribirDesarrollanSerializer

class DesarrollanViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticated]
    queryset = Desarrollan.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return LeerDesarrollanSerializer
        return escribirDesarrollanSerializer