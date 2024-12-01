from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.residuos.models import Residuos
from apps.trazabilidad.residuos.api.serializers import LeerResiduosSerializer, escribirResiduosSerializer

class ResiduosViewSet(ModelViewSet):
    queryset = Residuos.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return LeerResiduosSerializer
        return escribirResiduosSerializer