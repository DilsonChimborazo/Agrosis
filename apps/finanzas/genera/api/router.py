from rest_framework.routers import DefaultRouter
from apps.finanzas.genera.api.views import GeneraViewSet

router_Genera = DefaultRouter()
router_Genera.register(prefix="genera", basename="generan", viewset=GeneraViewSet)

