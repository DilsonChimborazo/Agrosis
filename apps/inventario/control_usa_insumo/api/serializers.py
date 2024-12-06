from rest_framework.serializers import ModelSerializer
from apps.inventario.control_usa_insumo.models import ControlUsaInsumo
from apps.inventario.insumo.api.serializers import InsumoSerializer
from apps.trazabilidad.control_fitosanitario.api.serializers import LeerControl_fitosanitarioSerializer

class LeerControlUsaInsumoSerializer (ModelSerializer):
    fk_id_insumo = InsumoSerializer ()
    fk_id_control_fitosanitario = LeerControl_fitosanitarioSerializer ()
    class Meta :
        model = ControlUsaInsumo
        fields = '__all__'

class ControlUsaInsumoSereializer(ModelSerializer):
    class Meta:
        model = ControlUsaInsumo
        fields = '__all__'   