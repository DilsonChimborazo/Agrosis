from rest_framework.routers import DefaultRouter
from apps.trazabilidad.actividad.api.views import ActividadViewSet

router_trazabilidad = DefaultRouter()
router_trazabilidad.register(prefix='actividad', viewset=ActividadViewSet, basename='actividad')