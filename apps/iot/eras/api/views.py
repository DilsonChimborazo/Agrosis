from rest_framework.viewsets import ModelViewSet
from apps.iot.eras.models import Eras
from apps.iot.eras.api.serializers import leerErasSerializer, escribirErasSerializer

class ErasViewSet(ModelViewSet):
    queryset = Eras.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return leerErasSerializer
        return escribirErasSerializer

