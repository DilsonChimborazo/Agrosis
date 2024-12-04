from rest_framework.viewsets import ModelViewSet
from apps.inventario.requiere.models import Requiere
from rest_framework.permissions import IsAutenticated
from apps.inventario.requiere.api.serializers import LeerRequiereSerializer

class RequiereViewset (ModelViewSet):
    queryset = Requiere.objects.all()
    permissions_clases = [IsAutenticated]
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrive']:
            return LeerRequiereSerializer 