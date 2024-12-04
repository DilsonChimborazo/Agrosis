from rest_framework.viewsets import ModelViewSet
from apps.finanzas.venta.models import Venta
from rest_framework.permissions import IsAutenticated
from apps.finanzas.venta.api.serializer import leerVentaSerializer, escribirVentaSerializer

class VentaViewSet(ModelViewSet):
    queryset = Venta.objects.all()
    permissions_clases = [IsAutenticated]
    
    def get_serializer_class(self):
        if self.action in ['list','retrive']:
            return leerGeneraSerializer
        return escribirVentaSerializer