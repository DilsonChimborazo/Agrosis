from rest_framework.viewsets import ModelViewSet
from apps.inventario.requiere.models import Requiere
from apps.inventario.requiere.api.serializers import LeerRequiereSerializer

class RequiereViewset (ModelViewSet):
    queryset = Requiere.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrive']:
            return LeerRequiereSerializer 