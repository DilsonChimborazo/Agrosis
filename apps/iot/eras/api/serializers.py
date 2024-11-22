from rest_framework.serializers import ModelSerializer
from apps.iot.eras.models import Eras
from apps.iot.lote.api.serializers import LoteSerializer


class ErasSerializer(ModelSerializer):
    fk_id_lote = LoteSerializer()
    class Meta:
        model = Eras
        fields = '__all__'
        