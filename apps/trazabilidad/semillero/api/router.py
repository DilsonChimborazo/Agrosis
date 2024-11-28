from rest_framework.routers import DefaultRouter
from apps.trazabilidad.semillero.api.views import SemilleroModelViewSet

# Crear routers específicos para el ViewSet de Semillero
routerSemillero = DefaultRouter()
routerSemillero.register(prefix='semilleros', viewset=SemilleroModelViewSet, basename='semilleros')

# Exportar los routers como un diccionario
routers = {
    'semilleros': routerSemillero,
}
