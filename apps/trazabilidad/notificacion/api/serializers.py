from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.notificacion.models import Notificacion
from apps.trazabilidad.programacion.api.serializers import LeerProgramacionSerializer

class LeerNotificacionSerializer(ModelSerializer):
    fk_id_programacion = LeerProgramacionSerializer()

    class Meta:
        model = Notificacion
        fields = '__all__'

class EscribirNotificacionSerializer(ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'
