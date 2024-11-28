from rest_framework.routers import DefaultRouter
from apps.trazabilidad.especie.api.views import EspecieModelViewSet

# Crear routers específicos para el ViewSet de Especie
routerEspecie = DefaultRouter()
routerEspecie.register(prefix='especies', viewset=EspecieModelViewSet, basename='especies')

# Exportar los routers como un diccionario
routers = {
    'especies': routerEspecie,
}
