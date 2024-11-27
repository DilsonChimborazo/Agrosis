from rest_framework.routers import DefaultRouter
from apps.trazabilidad.pea.api.views import PeaViewSet

router_pea = DefaultRouter()
router_pea.register(prefix='pea', viewset=PeaViewSet, basename='pea')