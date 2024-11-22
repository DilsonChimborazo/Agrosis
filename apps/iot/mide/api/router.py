from rest_framework.routers import DefaultRouter
from apps.iot.mide.api.views import MideViewSet

router_Mide = DefaultRouter()
router_Mide.register(prefix="mide", basename="mide", viewsets=MideViewSet)