from rest_framework.serializers import ModelSerializer
from apps.Finanzas.models import Venta  

class VentaSerializer(ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'  
