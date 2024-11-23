from rest_framework.viewsets import ModelViewSet
from apps.iot.mide.models import Mide
from apps.iot.mide.api.serializers import leerMideSerializer,escribirMideSerializer

class MideViewSet(ModelViewSet):
    queryset = Mide.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrive']:
            return leerMideSerializer
        return escribirMideSerializer
