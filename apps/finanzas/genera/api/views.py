from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAutenticated
from apps.finanzas.genera.models import Genera
from apps.finanzas.genera.api.serializer import leerGeneraSerializer, escribirGeneraSerializer

class GeneraViewSet(ModelViewSet):
    queryset = Genera.objects.all()
    permissions_clases = [IsAutenticated]
    
    def get_serializer_class(self):
        if self.action in ['list','retrive']:
            return leerGeneraSerializer
        return escribirGeneraSerializer