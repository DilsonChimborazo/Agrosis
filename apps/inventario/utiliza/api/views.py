from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAutenticated
from apps.inventario.utiliza.models import Utiliza
from apps.inventario.utiliza.api.serializers import LeerUtilizaSerializer

class RequiereViewset (ModelViewSet):
    queryset = Utiliza.objects.all()
    permissions_clases = [IsAutenticated]
    
    

    def get_serializer_class(self):
        if self.action in ['list', 'retrive']:
            return LeerUtilizaSerializer 