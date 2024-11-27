from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.cultivo.models import Cultivo
from apps.trazabilidad.especie.api.serializers import EspecieSerializer 

class CultivoSerializer(ModelSerializer):
    fk_id_especie = EspecieSerializer() 
    fk_id_semillero = SemilleroSerializer()
    class Meta:
        model = Cultivo
        fields = '__all__'

class escribirCultivoSerializer(ModelSerializer):
    class Meta:
        model = Cultivo
        fields = '__all__'