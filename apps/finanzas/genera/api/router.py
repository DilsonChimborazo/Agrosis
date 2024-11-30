from rest_framework.routers import DefaultRouter
from apps.finanzas.genera.api.views import GeneraViewSet

router_Genera = DefaultRouter()
router_genera.register(prefix="genera", basename="generan", viewset=GeneraViewSet)

urlpatterns = router_genera.urls