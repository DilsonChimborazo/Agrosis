from rest_framework.serializers import ModelSerializer
from apps.inventario.models import Insumos,Herramientas


class InsumosSerializer(ModelSerializer):
    class Meta:
        model = Insumos
        fields = '__all__'

class HerramientasSerializer(ModelSerializer):
    class Meta:
        model= Herramientas
        fields = '__all__'