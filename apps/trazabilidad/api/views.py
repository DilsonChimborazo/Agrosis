from rest_framework.viewsets import ModelViewSet
from apps.trazabilidad.models import *
from apps. trazabilidad.api.serializers import *


#p

class ActividadModelViewSet(ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class RealizaModelViewSet(ModelViewSet):
    queryset = Realiza.objects.all()
    serializer_class = RealizaSerializer

class EspecieModelViewSet(ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer

class TipoCultivoModelViewSet(ModelViewSet):
    queryset = TipoCultivo.objects.all()
    serializer_class = TipoCultivoSerializer

class SemilleroModelViewSet(ModelViewSet):
    queryset = Semillero.objects.all()
    serializer_class = SemilleroSerializer

class AsignacionActividadModelViewSet(ModelViewSet):
    queryset = AsignacionActividades.objects.all()
    serializer_class = AsignacionActividadSerializer

class ProgramacionModelViewSet(ModelViewSet):
    queryset = Programacion.objects.all()
    serializer_class = ProgramacionSerializer

class NotificacionModelViewSet(ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

class ControlUsoInsumoModelViewSet(ModelViewSet):
    queryset = ControlUsoInsumo.objects.all()
    serializer_class = ControlUsoInsumoSerializer

class CalendarioLunarModelViewSet(ModelViewSet):
    queryset = CalendarioLunar.objects.all()
    serializer_class = CalendarioLunarSerializer



#x


class UbicacionModelViewSet(ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    
class LoteModelViewSet(ModelViewSet):
    serializer_class = LoteSerializer
    queryset = Lote.objects.all()
    
class ErasModelViewSet(ModelViewSet):
    serializer_class = ErasSerializer
    queryset = Eras.objects.all()

class CultivoModelViewSet(ModelViewSet):
    serializer_class = CultivoSerializer
    queryset = Cultivo.objects.all()
    
class PlantacionModelViewSet(ModelViewSet):
    serializer_class = PlantacionSerializer
    queryset = Plantacion.objects.all()
    
class PeaModelViewSet(ModelViewSet):
    serializer_class = PeaSerializer
    queryset = Pea.objects.all()

class DesarrollanModelViewSet(ModelViewSet):
    serializer_class = DesarrollanSerializer
    queryset = Desarrollan.objects.all()

class Tipo_residuosModelViewSet(ModelViewSet):  
    serializer_class = Tipo_residuosSerializer
    queryset = Tipo_residuos.objects.all()

class ResiduosModelViewSet(ModelViewSet):
    serializer_class = ResiduosSerializer
    queryset = Residuos.objects.all()

class Control_fitosanitarioModelViewSet(ModelViewSet):
    serializer_class = Control_fitosanitarioSerializer
    queryset = Control_fitosanitario.objects.all()
      