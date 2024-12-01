from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.control_fitosanitario.models import Control_fitosanitario
from apps.trazabilidad.desarrollan.api.serializers import LeerDesarrollanSerializer 

class LeerControl_fitosanitarioSerializer(ModelSerializer):
    fk_id_desarrollan = LeerDesarrollanSerializer() 
    class Meta:
        model = Control_fitosanitario
        fields = '__all__'

class escribirControl_fitosanitarioSerializer(ModelSerializer):
    class Meta:
        model = Control_fitosanitario
        fields = '__all__'