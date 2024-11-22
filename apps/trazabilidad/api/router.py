from rest_framework.routers import DefaultRouter
from apps.trazabilidad.api.views import ActividadModelViewSet, RealizaModelViewSet, EspecieModelViewSet, TipoCultivoModelViewSet, SemilleroModelViewSet, AsignacionActividadModelViewSet, ProgramacionModelViewSet, NotificacionModelViewSet, ControlUsoInsumoModelViewSet, CalendarioLunarModelViewSet, UbicacionModelViewSet, LoteModelViewSet, ErasModelViewSet, PlantacionModelViewSet, DesarrollanModelViewSet, PeaModelViewSet, DesarrollanModelViewSet, Tipo_residuosModelViewSet, CultivoModelViewSet, ResiduosModelViewSet, Control_fitosanitarioModelViewSet

# Crear routers específicos para cada grupo de ViewSets

#p


router_actividad = DefaultRouter()
router_actividad.register(prefix='actividades', viewset=ActividadModelViewSet, basename='actividades')

router_realiza = DefaultRouter()
router_realiza.register(prefix='realiza', viewset=RealizaModelViewSet, basename='realiza')

router_especie = DefaultRouter()
router_especie.register(prefix='especies', viewset=EspecieModelViewSet, basename='especies')

router_tipo_cultivo = DefaultRouter()
router_tipo_cultivo.register(prefix='tipos_cultivo', viewset=TipoCultivoModelViewSet, basename='tipos_cultivo')

router_semillero = DefaultRouter()
router_semillero.register(prefix='semilleros', viewset=SemilleroModelViewSet, basename='semilleros')

router_asignacion_actividad = DefaultRouter()
router_asignacion_actividad.register(prefix='asignaciones_actividades', viewset=AsignacionActividadModelViewSet, basename='asignaciones_actividades')

router_programacion = DefaultRouter()
router_programacion.register(prefix='programaciones', viewset=ProgramacionModelViewSet, basename='programaciones')

router_notificacion = DefaultRouter()
router_notificacion.register(prefix='notificaciones', viewset=NotificacionModelViewSet, basename='notificaciones')

router_control_uso_insumo = DefaultRouter()
router_control_uso_insumo.register(prefix='control_uso_insumos', viewset=ControlUsoInsumoModelViewSet, basename='control_uso_insumos')

router_calendario_lunar = DefaultRouter()
router_calendario_lunar.register(prefix='calendario_lunar', viewset=CalendarioLunarModelViewSet, basename='calendario_lunar')


#x


router_ubicacion = DefaultRouter()
router_ubicacion.register(prefix='ubicacion',viewset= UbicacionModelViewSet, basename='ubicacion')

router_lote = DefaultRouter()
router_lote.register(prefix='lote',viewset= LoteModelViewSet, basename='lote')

router_eras = DefaultRouter()
router_eras.register(prefix='eras',viewset= ErasModelViewSet, basename='eras')

router_cultivo = DefaultRouter()
router_cultivo.register(prefix='cultivo',viewset= CultivoModelViewSet, basename='cultivo')

router_plantacion = DefaultRouter()
router_plantacion.register(prefix='plantacion',viewset= PlantacionModelViewSet, basename='plantacion')

router_pea = DefaultRouter()
router_pea.register(prefix='pea',viewset= PeaModelViewSet, basename='pea')

router_desarrollan = DefaultRouter()
router_desarrollan.register(prefix='desarrollan',viewset= DesarrollanModelViewSet, basename='desarrollan')

router_tipo_residuos = DefaultRouter()
router_tipo_residuos.register(prefix='tipo_residuos',viewset= Tipo_residuosModelViewSet, basename='tipo_residuos')

router_residuos = DefaultRouter()
router_residuos.register(prefix='residuos',viewset= ResiduosModelViewSet, basename='residuos')

router_control_fitosanitario = DefaultRouter()
router_control_fitosanitario.register(prefix='control_fitosanitario',viewset= Control_fitosanitarioModelViewSet, basename='control_fitosanitario')





# Exportar los routers como un diccionario
routers = {
    'actividades': router_actividad,
    'realiza': router_realiza,
    'especies': router_especie,
    'tipos_cultivo': router_tipo_cultivo,
    'semilleros': router_semillero,
    'asignaciones_actividades': router_asignacion_actividad,
    'programaciones': router_programacion,
    'notificaciones': router_notificacion,
    'control_uso_insumos': router_control_uso_insumo,
    'calendario_lunar': router_calendario_lunar,
    'ubicacion': router_ubicacion,
    'lote': router_lote,
    'eras': router_eras,
    'cultivo': router_cultivo,
    'plantacion': router_plantacion,
    'pea': router_pea,
    'desarrollan': router_desarrollan,
    'tipo_residuos': router_tipo_residuos,
    'residuos': router_residuos,
    'control_fitosanitario': router_control_fitosanitario,
}
