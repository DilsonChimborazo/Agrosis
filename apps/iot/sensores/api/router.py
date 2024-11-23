from rest_framework.routers import DefaultRouter
from apps.iot.sensores.api.views import SensoresViewSet

router_Sensores = DefaultRouter()
router_Sensores.register(prefix="sensores", basename="sensores", viewset=SensoresViewSet)
