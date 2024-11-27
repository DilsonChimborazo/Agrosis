from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.pea.models import Pea

class PeaSerializer(ModelSerializer):
    class Meta:
        model = Pea
        fields = '__all__'