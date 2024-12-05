from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.realiza.models import Realiza
from apps.trazabilidad.cultivo.api.serializers import LeerCultivoSerializer
from apps.trazabilidad.actividad.api.serializers import LeerActividadSerializer

class LeerRealizaSerializer(ModelSerializer):
    fk_id_cultivo = LeerCultivoSerializer()
    fk_id_actividad = LeerActividadSerializer()

    class Meta:
        model = Realiza
        fields = '__all__'

class EscribirRealizaSerializer(ModelSerializer):
    class Meta:
        model = Realiza
        fields = '__all__'
