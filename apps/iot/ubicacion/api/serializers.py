from rest_framework.serializers import ModelSerializer
from apps.iot.ubicacion.models import Ubicacion


class UbicacionSerializer(ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'
        

