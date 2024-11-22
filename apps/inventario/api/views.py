from rest_framework.viewsets import ModelViewSet
from apps.inventario.models import *
from apps.inventario.api.serializers import *



class InsumoViewset(ModelViewSet):
    queryset= Insumos.objects.all()
    serializer_class = InsumosSerializer


class HerramientasViewset(ModelViewSet):
    queryset=Herramientas.objects.all()
    serializer_class=HerramientasSerializer
    

class RequiereViewset(ModelViewSet):
    queryset=Requiere.objects.all()
    serializer_class=RequiereSerializer


class UtilizaViewset(ModelViewSet):
    queryset=Utiliza.objects.all()
    serializer_class=UtilizaSerializer

class ControlUsoInsumoModelViewSet(ModelViewSet):
    queryset = ControlUsoInsumo.objects.all()
    serializer_class = ControlUsoInsumoSerializer

