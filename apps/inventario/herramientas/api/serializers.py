from rest_framework.serializers import ModelSerializer
from apps.inventario.herramientas.models import Herramientas



class HerramientasSerializer(ModelSerializer):
    class Meta:
        model = Herramientas
        fields = '__all__'  