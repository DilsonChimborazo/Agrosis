from rest_framework.routers import DefaultRouter
from apps.trazabilidad.tipo_residuos.api.views import Tipo_residuosViewSet

router_tipo_residuos = DefaultRouter()
router_tipo_residuos.register(prefix='tipo_residuos', viewset=Tipo_residuosViewSet, basename='tipo_residuos')