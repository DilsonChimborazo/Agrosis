from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.desarrollan.models import Desarrollan
from apps.trazabilidad.desarrollan.api.serializers import LeerDesarrollanSerializer, escribirDesarrollanSerializer

class DesarrollanViewSet(ModelViewSet):
    queryset = Desarrollan.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return LeerDesarrollanSerializer
        return escribirDesarrollanSerializer