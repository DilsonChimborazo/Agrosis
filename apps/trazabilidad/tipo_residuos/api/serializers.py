from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.tipo_residuos.models import Tipo_residuos

class LeerTipo_residuosSerializer(ModelSerializer):
    class Meta:
        model = Tipo_residuos
        fields = '__all__'