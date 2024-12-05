from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.calendario_lunar.models import Calendario_lunar

class LeerCalendario_lunarSerializer(ModelSerializer):
    class Meta:
        model = Calendario_lunar
        fields = '__all__'

class EscribirCalendario_lunarSerializer(ModelSerializer):
    class Meta:
        model = Calendario_lunar
        fields = '__all__'
