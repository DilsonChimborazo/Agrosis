from rest_framework.serializers import ModelSerializer
from apps.inventario.herramientas.models import Herramientas



class HerramientasSereializer(ModelSerializer):
    class meta:
        model = Herramientas
        fields = '__all__'  