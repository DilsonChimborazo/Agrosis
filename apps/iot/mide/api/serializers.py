from rest_framework.serializers import ModelSerializer
from apps.iot.mide.models import Mide


class MideSerializer(ModelSerializer):
    class Meta:
        model = Mide
        fields = '__all__'
        

