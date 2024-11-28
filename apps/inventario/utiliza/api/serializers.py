from rest_framework.serializers import ModelSerializer
from apps.inventario.utiliza.models import Utiliza
from apps.inventario.utiliza.api.serializers import LeerUtilizaSerializer
from apps.trazabilidad.Asignacion_actividades.api.Serializers import Asignacion_actividades

class LeerUtilizaSerializer (ModelSerializer):
     fk_id_insumo = LeerUtilizaSerializer ()
     fk_id_asignacion_actividades =  Asignacion_actividades()
     class meta :
         model = LeerUtilizaSerializer 
         fields = '__all__'

class UtilizaSereializer(ModelSerializer):
    class meta:
        model = Utiliza
        fields = '__all__'  