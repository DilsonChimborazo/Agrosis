from rest_framework.viewsets import ModelViewSet
from apps.finanzas.venta.models import Venta
from rest_framework.permissions import IsAuthenticated
from apps.finanzas.venta.api.serializers import leerVentaSerializer, escribirVentaSerializer

class VentaViewSet(ModelViewSet):
    queryset = Venta.objects.all()
    permissions_clases = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['list','retrive']:
            return leerVentaSerializer
        return escribirVentaSerializer