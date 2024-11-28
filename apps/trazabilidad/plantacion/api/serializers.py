from rest_framework.serializers import ModelSerializer
from apps.trazabilidad.plantacion.models import Plantacion
from apps.trazabilidad.cultivo.api.serializers import CultivoSerializer 
from apps.trazabilidad.eras.api.serializers import ErasSerializer 

class PlantacionSerializer(ModelSerializer):
    fk_id_era = leerErasSerializer()
    fk_id_cultivo = CultivoSerializer()
    class Meta:
        model = Plantacion
        fields = '__all__'
        
class escribirPlantacionSerializer(ModelSerializer):
    class Meta:
        model = Plantacion
        fields = '__all__'
