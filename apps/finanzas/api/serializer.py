from rest_framework.serializers import ModelSerializer
from apps.finanzas.models import * 

class VentaSerializer(ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'  

class ProduccionSerializer(ModelSerializer):
    class Meta:
        model = Produccion
        fields = '__all__'  

class GeneraSerializer(ModelSerializer):
    class Meta:
        model = Genera
        fields = '__all__'  
