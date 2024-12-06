from rest_framework.routers import DefaultRouter
from apps.iot.lote.api.views import LoteViewSet

router_Lote = DefaultRouter()
router_Lote.register(prefix="lote", basename="Lote", viewset=LoteViewSet)
