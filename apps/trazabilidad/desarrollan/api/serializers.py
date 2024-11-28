from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.desarrollan.models import Desarrollan
from apps.trazabilidad.cultivo.api.serializers import CultivoSerializer 
from apps.trazabilidad.pea.api.serializers import PeaSerializer 

class DesarrollanSerializer(ModelSerializer):
    fk_id_cultivo = CultivoSerializer() 
    fk_id_pea = PeaSerializer()
    class Meta:
        model = Desarrollan
        fields = '__all__'

class escribirDesarrollanSerializer(ModelSerializer):
    class Meta:
        model = Desarrollan
        fields = '__all__'