from rest_framework.routers import DefaultRouter
from apps.iot.mide.api.views import MideViewSet
from apps.iot.sensores.api.views import SensoresViewSet 
from apps.iot.ubicacion.api.views import  UbicacionViewSet
from apps.iot.lote.api.views import LoteViewSet
from apps.iot.eras.api.views import ErasViewSet


router = DefaultRouter()
router.register(prefix="mide", viewset=MideViewSet)
router.register(prefix="sensores", viewset=SensoresViewSet)
router.register(prefix="ubicacion",  viewset=UbicacionViewSet)
router.register(prefix="lote", viewset=LoteViewSet)
router.register(prefix="eras", viewset=ErasViewSet)