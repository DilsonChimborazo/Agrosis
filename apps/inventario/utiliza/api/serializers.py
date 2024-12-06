from rest_framework.serializers import ModelSerializer
from apps.inventario.utiliza.models import Utiliza
from apps.inventario.insumo.api.serializers import InsumoSerializer
from apps.trazabilidad.asignacion_actividades.api.serializers import Asignacion_actividades

class LeerUtilizaSerializer (ModelSerializer):
    fk_id_insumo = InsumoSerializer()
    fk_id_asignacion_actividades =  Asignacion_actividades()
    class Meta :
        model = Utiliza 
        fields = '__all__'

class UtilizaSereializer(ModelSerializer):
    class Meta:
        model = Utiliza
        fields = '__all__'  