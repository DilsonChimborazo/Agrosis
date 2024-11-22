from rest_framework.routers import DefaultRouter
from apps.sensores.api.views import SensoresViewSet,MideViewSet

router_Sensores = DefaultRouter()
router_Sensores.register(prefix="sensores", basename="sensores", viewsets=SensoresViewSet)

router_Mide = DefaultRouter()
router_Mide.register(prefix="mide", basename="mide", viewsets=MideViewSet)