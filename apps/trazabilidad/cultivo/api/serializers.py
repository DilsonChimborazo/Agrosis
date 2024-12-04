from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.cultivo.models import Cultivo
from apps.trazabilidad.especie.api.serializers import LeerEspecieSerializer 
from apps.trazabilidad.semillero.api.serializers import LeerSemilleroSerializer

class LeerCultivoSerializer(ModelSerializer):
    fk_id_especie = LeerEspecieSerializer() 
    fk_id_semillero = LeerSemilleroSerializer()
    class Meta:
        model = Cultivo
        fields = '__all__'

class EscribirCultivoSerializer(ModelSerializer):
    class Meta:
        model = Cultivo
        fields = '__all__'