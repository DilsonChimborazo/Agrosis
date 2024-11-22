from rest_framework.serializers import ModelSerializer
from apps.sensores.models import Sensores, Mide

class SensoresSerializer(ModelSerializer):
    class Meta:
        model = Sensores
        fields = '__all__'

class MideSerializer(ModelSerializer):
    class Meta:
        model = Mide
        fields = '__all__'
        

