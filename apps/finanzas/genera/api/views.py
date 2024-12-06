from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.finanzas.genera.models import Genera
from apps.finanzas.genera.api.serializers import leerGeneraSerializer, escribirGeneraSerializer

class GeneraViewSet(ModelViewSet):
    queryset = Genera.objects.all()
    permissions_clases = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['list','retrive']:
            return leerGeneraSerializer
        return escribirGeneraSerializer