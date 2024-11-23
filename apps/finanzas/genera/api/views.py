from rest_framework.viewsets import ModelViewSet
from apps.finanzas.genera.models import Genera
from apps.finanzas.genera.api.serializer import leerGeneraSerializer, escribirGeneraSerializer

class GeneraViewSet(ModelViewSet):
    queryset = Genera.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrive']:
            return leerGeneraSerializer
        return escribirGeneraSerializer