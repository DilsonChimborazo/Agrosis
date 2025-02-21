from rest_framework.routers import DefaultRouter
from apps.iot.eras.api.views import ErasViewSet

router_Eras = DefaultRouter()
router_Eras.register(prefix="eras", basename="eras", viewset=ErasViewSet)
