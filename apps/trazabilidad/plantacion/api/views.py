from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.trazabilidad.plantacion.models import Plantacion
from apps.trazabilidad.plantacion.api.serializers import LeerPlantacionSerializer, escribirPlantacionSerializer

class PlantacionViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticated]
    queryset = Plantacion.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return LeerPlantacionSerializer
        return escribirPlantacionSerializer