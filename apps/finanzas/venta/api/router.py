from rest_framework.routers import DefaultRouter
from apps.finanzas.venta.api.views import VentaViewSet

router_venta = DefaultRouter()
router_venta.register(prefix="venta", basename="ventas", viewset=VentaViewSet)

