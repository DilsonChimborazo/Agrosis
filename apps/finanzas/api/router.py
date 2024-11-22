from rest_framework.routers import DefaultRouter
from apps.finanzas.api.views import VentaViewSet

router_ventas = DefaultRouter()
router_ventas.register(prefix="ventas", basename="venta", viewset=VentaViewSet)