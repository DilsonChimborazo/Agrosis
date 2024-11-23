from rest_framework.serializers import ModelSerializer
from apps.finanzas.genera.models import Genera

claas leerGeneraSerializer(ModelSerializer):
    fk_id_produccion = ProduccionSerializer()
    fk_id_cultivo = CultivoSerializer()
    class Meta:
        model = Genera
        fields = '__all__'  

class escribirGeneraSerializer(ModelSerializer):
    class Meta:
        model = Genera
        fields = '__all__'