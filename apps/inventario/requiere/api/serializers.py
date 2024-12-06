from rest_framework.serializers import ModelSerializer
from apps.inventario.requiere.models import Requiere
from apps.inventario.herramientas.api.serializers import HerramientasSerializer
from apps.trazabilidad.asignacion_actividades.api.serializers import Asignacion_actividades

class LeerRequiereSerializer (ModelSerializer):
    fk_Id_herramientas = HerramientasSerializer ()
    fk_id_asignaciona_actividades =  Asignacion_actividades()
    class Meta :
        model = Requiere
        fields = '__all__'

class RequiereSereializer(ModelSerializer):
    class Meta:
        model = Requiere
        fields = '__all__'  