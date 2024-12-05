from rest_framework.routers import DefaultRouter
from apps.trazabilidad.programacion.api.views import ProgramacionModelViewSet

# Crear routers específicos para el ViewSet de Programacion
routerProgramacion = DefaultRouter()
routerProgramacion.register(prefix='programaciones', viewset=ProgramacionModelViewSet, basename='programaciones')

# Exportar los routers como un diccionario
routers = {
    'programaciones': routerProgramacion,
}
