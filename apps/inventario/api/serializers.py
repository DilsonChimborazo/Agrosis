from rest_framework.serializers import ModelSerializer
from apps.inventario.models import *


class InsumosSerializer(ModelSerializer):
    class Meta:
        model = Insumos
        fields = '__all__'

class HerramientasSerializer(ModelSerializer):
    class Meta:
        model= Herramientas
        fields = '__all__'

class RequiereSerializer(ModelSerializer):
    class Meta:
        model= Requiere
        fields = '__all__'

class UtilizaSerializer(ModelSerializer):
    class Meta:
        model= Utiliza
        fields = '__all__'

class ControlUsoInsumoSerializer(ModelSerializer):
    class Meta:
        model = ControlUsoInsumo
        fields = '__all__'