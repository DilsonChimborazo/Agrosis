from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.semillero.models import Semillero

class LeerSemilleroSerializer(ModelSerializer):
    class Meta:
        model = Semillero
        fields = '__all__'

class EscribirSemilleroSerializer(ModelSerializer):
    class Meta:
        model = Semillero
        fields = '__all__'
