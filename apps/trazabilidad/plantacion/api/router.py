from rest_framework.routers import DefaultRouter
from apps.plantacion.api.views import *

# Crear routers específicos para cada grupo de ViewSets

#p


router_trazabilidad = DefaultRouter()
router_trazabilidad.register(prefix='actividades', viewset=ActividadModelViewSet, basename='actividades')
router_trazabilidad.register(prefix='realiza', viewset=RealizaModelViewSet, basename='realiza')
router_trazabilidad.register(prefix='especies', viewset=EspecieModelViewSet, basename='especies')
router_trazabilidad.register(prefix='tipos_cultivo', viewset=TipoCultivoModelViewSet, basename='tipos_cultivo')
router_trazabilidad.register(prefix='semilleros', viewset=SemilleroModelViewSet, basename='semilleros')
router_trazabilidad.register(prefix='asignaciones_actividades', viewset=AsignacionActividadModelViewSet, basename='asignaciones_actividades')
router_trazabilidad.register(prefix='programaciones', viewset=ProgramacionModelViewSet, basename='programaciones')
router_trazabilidad.register(prefix='notificaciones', viewset=NotificacionModelViewSet, basename='notificaciones')
router_trazabilidad.register(prefix='calendario_lunar', viewset=CalendarioLunarModelViewSet, basename='calendario_lunar')
router_trazabilidad.register(prefix='ubicacion',viewset= UbicacionModelViewSet, basename='ubicacion')
router_trazabilidad.register(prefix='lote',viewset= LoteModelViewSet, basename='lote')
router_trazabilidad.register(prefix='eras',viewset= ErasModelViewSet, basename='eras')
router_trazabilidad.register(prefix='cultivo',viewset= CultivoModelViewSet, basename='cultivo')
router_trazabilidad.register(prefix='plantacion',viewset= PlantacionModelViewSet, basename='plantacion')
router_trazabilidad.register(prefix='pea',viewset= PeaModelViewSet, basename='pea')
router_trazabilidad.register(prefix='desarrollan',viewset= DesarrollanModelViewSet, basename='desarrollan')
router_trazabilidad.register(prefix='tipo_residuos',viewset= Tipo_residuosModelViewSet, basename='tipo_residuos')
router_trazabilidad.register(prefix='residuos',viewset= ResiduosModelViewSet, basename='residuos')
router_trazabilidad.register(prefix='control_fitosanitario',viewset= Control_fitosanitarioModelViewSet, basename='control_fitosanitario')



