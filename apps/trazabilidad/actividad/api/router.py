from rest_framework.routers import DefaultRouter
from apps.trazabilidad.actividad.api.views import ActividadViewSet

router_actividad = DefaultRouter()
router_actividad.register(prefix='actividad', viewset=ActividadViewSet, basename='actividad')