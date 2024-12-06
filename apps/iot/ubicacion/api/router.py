from rest_framework.routers import DefaultRouter
from apps.iot.ubicacion.api.views import UbicacionViewSet

router_Ubicacion = DefaultRouter()
router_Ubicacion.register(prefix="ubicacion", basename="ubicacion", viewset=UbicacionViewSet)


