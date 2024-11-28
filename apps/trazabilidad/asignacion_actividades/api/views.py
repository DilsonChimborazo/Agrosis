from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.asignacion_actividades.models import Asignacion_actividades
from apps.trazabilidad.asignacion_actividades.api.serializers import LeerAsignacion_actividadesSerializer, EscribirAsignacion_actividadesSerializer

class Asignacion_actividadesModelViewSet(ModelViewSet):
    queryset = Asignacion_actividades.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LeerAsignacion_actividadesSerializer
        return EscribirAsignacion_actividadesSerializer
