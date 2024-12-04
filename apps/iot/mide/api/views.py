from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.iot.mide.models import Mide
from apps.iot.mide.api.serializers import leerMideSerializer,escribirMideSerializer

class MideViewSet(ModelViewSet):
    queryset = Mide.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['list','retrive']:
            return leerMideSerializer
        return escribirMideSerializer
