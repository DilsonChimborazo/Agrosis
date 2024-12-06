from rest_framework.serializers import ModelSerializer
from apps.inventario.insumo.models import Insumo


class InsumoSerializer(ModelSerializer):
    class Meta:
        model = Insumo
        fields = '__all__'  