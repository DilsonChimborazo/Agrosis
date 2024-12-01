from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.actividad.models import Actividad

class LeerActividadSerializer(ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'