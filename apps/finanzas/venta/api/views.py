from rest_framework.viewsets import ModelViewSet
from apps.finanzas.venta.models import Venta
from apps.finanzas.venta.api.serializer import leerVentaSerializer, escribirVentaSerializer

class VentaViewSet(ModelViewSet):
    queryset = Venta.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrive']:
            return leerGeneraSerializer
        return escribirVentaSerializer