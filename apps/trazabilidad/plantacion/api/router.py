from rest_framework.routers import DefaultRouter
from apps.trazabilidad.plantacion.api.views import PlantacionViewSet

router_plantacion = DefaultRouter()
router_plantacion.register(prefix='plantacion', viewset=PlantacionViewSet, basename='plantacion')
