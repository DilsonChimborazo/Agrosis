from rest_framework.routers import DefaultRouter
from apps.trazabilidad.cultivo.api.views import CultivoViewSet

router_cultivo = DefaultRouter()
router_cultivo.register(prefix='cultivo', viewset=CultivoViewSet, basename='cultivo')