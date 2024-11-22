from rest_framework.routers import DefaultRouter
from apps.finanzas.api.views import *

router_ventas = DefaultRouter()
router_ventas.register(prefix="ventas", basename="venta", viewset=VentaViewSet)
router_ventas.register(prefix="Produccion", basename="Produccion", viewset=ProduccionViewSet)
router_ventas.register(prefix="Genera", basename="Genera", viewset=GeneraViewSet)