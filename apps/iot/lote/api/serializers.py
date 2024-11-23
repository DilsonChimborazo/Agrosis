from rest_framework.serializers import ModelSerializer
from apps.iot.lote.models import Lote
from apps.iot.ubicacion.api.serializers import UbicacionSerializer

class leerLoteSerializer(ModelSerializer):
    fk_id_ubicacion = UbicacionSerializer()
    class Meta:
        model = Lote
        fields = '__all__'


class escribirLoteSerializer(ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

        

