from rest_framework.serializers import ModelSerializer
from apps.finanzas.genera.models import Genera
from apps.finanzas.produccion.api.serializers import ProduccionSerializer
from apps.trazabilidad.cultivo.api.serializers import LeerCultivoSerializer

class leerGeneraSerializer(ModelSerializer):
    fk_id_produccion = ProduccionSerializer()
    fk_id_cultivo = LeerCultivoSerializer()
    class Meta:
        model = Genera
        fields = '__all__'  

class escribirGeneraSerializer(ModelSerializer):
    class Meta:
        model = Genera
        fields = '__all__'