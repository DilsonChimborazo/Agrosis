from rest_framework.serializers import ModelSerializer
from apps.finanzas.produccion.models import Produccion

class ProduccionSerializer(ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'  