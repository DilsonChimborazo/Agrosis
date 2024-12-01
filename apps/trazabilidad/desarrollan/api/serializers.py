from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.desarrollan.models import Desarrollan
from apps.trazabilidad.cultivo.api.serializers import LeerCultivoSerializer 
from apps.trazabilidad.pea.api.serializers import LeerPeaSerializer 

class LeerDesarrollanSerializer(ModelSerializer):
    fk_id_cultivo = LeerCultivoSerializer() 
    fk_id_pea = LeerPeaSerializer()
    class Meta:
        model = Desarrollan
        fields = '__all__'

class escribirDesarrollanSerializer(ModelSerializer):
    class Meta:
        model = Desarrollan
        fields = '__all__'