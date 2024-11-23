from rest_framework.serializers import ModelSerializer
from apps.iot.eras.models import Eras
from apps.iot.lote.api.serializers import leerLoteSerializer 

class leerErasSerializer(ModelSerializer):
    fk_id_lote = leerLoteSerializer()  
    class Meta:
        model = Eras
        fields = '__all__'

class escribirErasSerializer(ModelSerializer):
    class Meta:
        model = Eras
        fields = '__all__'
        
