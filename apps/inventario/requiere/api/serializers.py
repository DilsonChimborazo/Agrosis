from rest_framework.serializers import ModelSerializer
from apps.inventario.requiere.models import Requiere
from apps.inventario.herramientas.api.serializers import HerramientasSereializer
from apps.trazabilidad.asignacion_actividades.api.serializers import Asignacion_actividades

class LeerRequiereSerializer (ModelSerializer):
    fk_Id_herramientas = HerramientasSereializer ()
    fk_id_asignacion_actividades =  Asignacion_actividades()
    class meta :
        model = Requiere
        fields = '__all__'

class RequiereSereializer(ModelSerializer):
    class meta:
        model = Requiere
        fields = '__all__'  