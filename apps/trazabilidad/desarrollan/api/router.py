from rest_framework.routers import DefaultRouter
from apps.trazabilidad.desarrollan.api.views import DesarrollanViewSet

router_desarrollan = DefaultRouter()
router_desarrollan.register(prefix='desarrollan', viewset=DesarrollanViewSet, basename='desarrollan')