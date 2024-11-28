from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.residuos.models import Residuos
from apps.trazabilidad.cultivo.api.serializers import CultivoSerializer 
from apps.trazabilidad.tipo_residuos.api.serializers import Tipo_residuosSerializer 

class ResiduosSerializer(ModelSerializer):
    fk_id_cultivo = CultivoSerializer() 
    fk_id_tipo_residuos = Tipo_residuosSerializer()
    class Meta:
        model = Residuos
        fields = '__all__'

class escribirResiduosSerializer(ModelSerializer):
    class Meta:
        model = Residuos
        fields = '__all__'