from rest_framework.viewsets import ModelViewSet
from apps.inventario.utiliza.models import Utiliza
from apps.inventario.utiliza.api.serializers import LeerUtilizaSerializer

class RequiereViewset (ModelViewSet):
    queryset = Utiliza.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrive']:
            return LeerUtilizaSerializer 