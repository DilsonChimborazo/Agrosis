from rest_framework.routers import DefaultRouter
from apps.trazabilidad.asignacion_actividades.api.views import Asignacion_actividadesModelViewSet
from django.urls import re_path
from apps.trazabilidad.asignacion_actividades.api.consumer import Asignacion_actividadesConsumer

# Crear routers específicos para cada grupo de ViewSets
routerAsignacion_actividades = DefaultRouter()
routerAsignacion_actividades.register(prefix='asignaciones_actividades', viewset=Asignacion_actividadesModelViewSet, basename='asignaciones_actividades')

websocket_urlpatterns = [
    re_path(r'ws/asignacion_actividades/$', Asignacion_actividadesConsumer.as_asgi()),
]