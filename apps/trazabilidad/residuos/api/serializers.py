from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.residuos.models import Residuos
from apps.trazabilidad.cultivo.api.serializers import LeerCultivoSerializer 
from apps.trazabilidad.tipo_residuos.api.serializers import LeerTipo_residuosSerializer 

class LeerResiduosSerializer(ModelSerializer):
    fk_id_cultivo = LeerCultivoSerializer() 
    fk_id_tipo_residuos = LeerTipo_residuosSerializer()
    class Meta:
        model = Residuos
        fields = '__all__'

class escribirResiduosSerializer(ModelSerializer):
    class Meta:
        model = Residuos
        fields = '__all__'