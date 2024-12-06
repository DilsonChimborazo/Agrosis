from rest_framework.routers import DefaultRouter
from apps.finanzas.produccion.api.views import ProduccionViewSet

router_produccion = DefaultRouter()
router_produccion.register(prefix="produccion", basename="producciones", viewset=ProduccionViewSet)

