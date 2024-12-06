from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.asignacion_actividades.models import Asignacion_actividades
from apps.trazabilidad.actividad.api.serializers import LeerActividadSerializer
from apps.usuarios.usuario.api.serializer import LeerUsuarioSerializer

class LeerAsignacion_actividadesSerializer(ModelSerializer):
    fk_id_actividad = LeerActividadSerializer()
    id_identificacion = LeerUsuarioSerializer()
    
    class Meta:
        model = Asignacion_actividades
        fields = '__all__'


class EscribirAsignacion_actividadesSerializer(ModelSerializer):
    class Meta:
        model = Asignacion_actividades
        fields = '__all__'
