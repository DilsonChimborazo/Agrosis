from rest_framework.serializers import ModelSerializer
from apps.iot.sensores.models import Sensores

class SensoresSerializer(ModelSerializer):
    class Meta:
        model = Sensores
        fields = '__all__'


