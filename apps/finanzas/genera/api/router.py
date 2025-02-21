
from rest_framework.routers import DefaultRouter
from apps.finanzas.genera.api.views import GeneraViewSet
from apps.finanzas.genera.api.consumer import GeneraConsumer




router_Genera = DefaultRouter()
router_Genera.register(prefix="genera", basename="genera", viewset=GeneraViewSet)

