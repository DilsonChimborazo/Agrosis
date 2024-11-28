from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.tipo_cultivo.models import Tipo_cultivo

class LeerTipo_cultivoSerializer(ModelSerializer):
    class Meta:
        model = Tipo_cultivo
        fields = '__all__'

class EscribirTipo_cultivoSerializer(ModelSerializer):
    class Meta:
        model = Tipo_cultivo
        fields = '__all__'
