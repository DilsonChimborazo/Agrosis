from rest_framework.viewsets import ModelViewSet
from apps.inventario.models import Insumos, Herramientas
from apps.inventario.api.serializers import InsumosSerializer,HerramientasSerializer
from rest_framework.permissions import IsAuthenticated
from apps.inventario.api.permissions import Permiso


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
    serializer_class=HerramientasSerializer
    
class Control_Usa_InsumosViewset(ModelViewSet):
    queryset=Control_Usa_Insumos.objects.all()
    serializer_class=HerramientasSerializer 
  