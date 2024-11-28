from rest_framework.routers import DefaultRouter
from apps.trazabilidad.realiza.api.views import RealizaModelViewSet

# Crear routers específicos para el ViewSet de Realiza
routerRealiza = DefaultRouter()
routerRealiza.register(prefix='realiza', viewset=RealizaModelViewSet, basename='realiza')

# Exportar los routers como un diccionario
routers = {
    'realiza': routerRealiza,
}
