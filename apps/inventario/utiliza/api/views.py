from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.inventario.utiliza.models import Utiliza
from apps.inventario.utiliza.api.serializers import LeerUtilizaSerializer

class UtilizaViewset (ModelViewSet):
    queryset = Utiliza.objects.all()
    permissions_clases = [IsAuthenticatedOrReadOnly]
    
    

    def get_serializer_class(self):
        if self.action in ['list', 'retrive']:
            return LeerUtilizaSerializer 