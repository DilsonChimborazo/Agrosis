from rest_framework.routers import DefaultRouter
from apps.trazabilidad.residuos.api.views import ResiduosViewSet

router_residuos = DefaultRouter()
router_residuos.register(prefix='residuos', viewset=ResiduosViewSet, basename='residuos')