from rest_framework.serializers import ModelSerializer
from apps.inventario.requiere.models import Requiere
from apps.inventario.requiere.api.serializers import LeerRequiereSerializer
from apps.trazabilidad.Asignacion_actividades.api.Serializers import Asignacion_actividades

class LeerRequiereSerializer (ModelSerializer):
     fk_Id_herramientas = LeerRequiereSerializer ()
     fk_id_asignacion_actividades =  Asignacion_actividades()
     class meta :
         model = LeerRequiereSerializer
         fields = '__all__'

class RequiereSereializer(ModelSerializer):
    class meta:
        model = Requiere
        fields = '__all__'  