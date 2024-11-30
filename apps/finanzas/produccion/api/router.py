from rest_framework.routers import DefaultRouter
from apps.finanzas.produccion.api.views import produccionViewSet

router_produccion = DefaultRouter()
router_produccionregister(prefix="produccion", basename="producciones", viewset=ProduccionViewSet)

urlpatterns = router_produccion.urls