from rest_framework.serializers import ModelSerializer
from apps.finanzas.venta.models import Venta 

claas leerVentaSerializer(ModelSerializer):
    fk_id_produccion = ProduccionSerializer()
    class Meta:
        model = Venta
        fields = '__all__'  

class escribirVentaSerializer(ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'  