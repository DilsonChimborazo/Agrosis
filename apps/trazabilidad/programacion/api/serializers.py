from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.programacion.models import Programacion
from apps.trazabilidad.asignacion_actividades.api.serializers import LeerAsignacion_actividadesSerializer
from apps.trazabilidad.calendario_lunar.api.serializers import LeerCalendario_lunarSerializer

class LeerProgramacionSerializer(ModelSerializer):
    fk_id_asignacionActividades = LeerAsignacion_actividadesSerializer()
    fk_id_calendario = LeerCalendario_lunarSerializer()

    class Meta:
        model = Programacion
        fields = '__all__'

class EscribirProgramacionSerializer(ModelSerializer):
    class Meta:
        model = Programacion
        fields = '__all__'
