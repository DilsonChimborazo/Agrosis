from rest_framework.serializers import ModelSerializer
from apps.iot.mide.models import Mide
from apps.iot.sensores.api.serializers import SensoresSerializer
from apps.iot.eras.api.serializers import ErasSerializer


class MideSerializer(ModelSerializer):
    fk_id_sensor = SensoresSerializer
    fk_id_era = ErasSerializer
    class Meta:
        model = Mide
        fields = '__all__'
        

