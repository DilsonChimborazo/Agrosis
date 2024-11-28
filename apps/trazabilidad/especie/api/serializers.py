from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.especie.models import Especie
from apps.trazabilidad.tipo_cultivo.api.serializers import LeerTipo_cultivoSerializer

class LeerEspecieSerializer(ModelSerializer):
    fk_id_tipo_cultivo = LeerTipo_cultivoSerializer()

    class Meta:
        model = Especie
        fields = '__all__'

class EscribirEspecieSerializer(ModelSerializer):
    class Meta:
        model = Especie
        fields = '__all__'
