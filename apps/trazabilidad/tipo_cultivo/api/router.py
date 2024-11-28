from rest_framework.routers import DefaultRouter
from apps.trazabilidad.tipo_cultivo.api.views import Tipo_cultivoModelViewSet

# Crear routers específicos para el ViewSet de Tipo_cultivo
routerTipo_cultivo = DefaultRouter()
routerTipo_cultivo.register(prefix='tipos_cultivo', viewset=Tipo_cultivoModelViewSet, basename='tipos_cultivo')

# Exportar los routers como un diccionario
routers = {
    'tipos_cultivo': routerTipo_cultivo,
}
