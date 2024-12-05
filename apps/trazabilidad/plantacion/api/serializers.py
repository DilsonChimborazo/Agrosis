from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.plantacion.models import Plantacion
from apps.trazabilidad.cultivo.api.serializers import LeerCultivoSerializer 
from apps.iot.eras.api.serializers import leerErasSerializer

class LeerPlantacionSerializer(ModelSerializer):
    fk_id_era = leerErasSerializer()
    fk_id_cultivo = LeerCultivoSerializer()
    class Meta:
        model = Plantacion
        fields = '__all__'
        
class escribirPlantacionSerializer(ModelSerializer):
    class Meta:
        model = Plantacion
        fields = '__all__'
