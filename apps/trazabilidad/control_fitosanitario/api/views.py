from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.trazabilidad.control_fitosanitario.models import Control_fitosanitario
from apps.trazabilidad.control_fitosanitario.api.serializers import LeerControl_fitosanitarioSerializer, escribirControl_fitosanitarioSerializer

class Control_fitosanitarioViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticatedOrReadOnly]
    queryset = Control_fitosanitario.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return LeerControl_fitosanitarioSerializer
        return escribirControl_fitosanitarioSerializer