from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.control_fitosanitario.models import Control_fitosanitario
from apps.trazabilidad.control_fitosanitario.api.serializers import Control_fitosanitarioSerializer, escribirControl_fitosanitarioSerializer

class Control_fitosanitarioViewSet(ModelViewSet):
    queryset = Control_fitosanitario.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return Control_fitosanitarioSerializer
        return escribirControl_fitosanitarioSerializer