from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.trazabilidad.notificacion.models import Notificacion
from apps.trazabilidad.notificacion.api.serializers import LeerNotificacionSerializer, EscribirNotificacionSerializer

class NotificacionModelViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticatedOrReadOnly]
    queryset = Notificacion.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LeerNotificacionSerializer
        return EscribirNotificacionSerializer
