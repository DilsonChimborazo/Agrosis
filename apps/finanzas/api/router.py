from rest_framework.routers import DefaultRouter
from apps.finanzas.api.views import VentaViewSet

router_venta = DefaultRouter()
router_venta.register(prefix="ventas", basename="venta", viewset=VentaViewSet)