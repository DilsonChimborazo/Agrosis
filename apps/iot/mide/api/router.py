from rest_framework.routers import DefaultRouter
from apps.iot.mide.api.views import MideViewSet

router_mide = DefaultRouter()
router_mide.register(prefix="mide",basename="mide", viewset=MideViewSet)

