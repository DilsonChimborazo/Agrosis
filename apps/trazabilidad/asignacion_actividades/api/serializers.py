from rest_framework.serializers import ModelSerializer
from asignacion_actividades.models import Asignacion_actividades
from apps.trazabilidad.actividades.api.serializers import LeerActividadSerializer
from apps.usuario.identificacion.api.serializers import LeerIdentificacionSerializer

class LeerAsignacion_actividadesSerializer(ModelSerializer):
    fk_id_actividad = LeerActividadSerializer()
    id_identificacion = LeerIdentificacionSerializer()
    
    class Meta:
        model = Asignacion_actividades
        fields = '__all__'


class EscribirAsignacion_actividadesSerializer(ModelSerializer):
    class Meta:
        model = Asignacion_actividades
        fields = '__all__'
