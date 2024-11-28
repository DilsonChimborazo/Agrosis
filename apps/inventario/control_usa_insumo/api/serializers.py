from rest_framework.serializers import ModelSerializer
from apps.inventario.control_usa_insumo.models import ControlUsaInsumo
from apps.inventario.insumo.api.serializers import LeerInsumoSerializer
from apps.trazabilidad.control_fitosanitario.api.serializers import Control_fitosanitarioSerializer

class LeerControlUsaInsumoSerializer (ModelSerializer):
     fk_id_insumo = LeerInsumoSerializer ()
     fk_id_control_fitosanitario = Control_fitosanitarioSerializer ()
     class meta :
         model = ControlUsaInsumo
         fields = '__all__'

class ControlUsaInsumoSereializer(ModelSerializer):
    class meta:
        model = ControlUsaInsumo
        fields = '__all__'   