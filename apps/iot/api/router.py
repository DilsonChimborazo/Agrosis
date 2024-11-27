from rest_framework.routers import DefaultRouter
from apps.iot.api.views import SensoresViewSet,MideViewSet

router_iot = DefaultRouter()
router_iot.register(prefix="sensores", basename="sensores", viewset=SensoresViewSet)
router_iot.register(prefix="mide", basename="mide", viewset=MideViewSet)