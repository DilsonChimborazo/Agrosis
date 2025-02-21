from rest_framework.routers import DefaultRouter
from apps.trazabilidad.asignacion_actividades.api.views import Asignacion_actividadesModelViewSet

# Crear routers específicos para cada grupo de ViewSets
routerAsignacion_actividades = DefaultRouter()
routerAsignacion_actividades.register(prefix='asignaciones_actividades', viewset=Asignacion_actividadesModelViewSet, basename='asignaciones_actividades')

