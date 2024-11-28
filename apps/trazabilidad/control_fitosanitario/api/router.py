from rest_framework.routers import DefaultRouter
from apps.trazabilidad.control_fitosanitario.api.views import Control_fitosanitarioViewSet

router_control_fitosanitario = DefaultRouter()
router_control_fitosanitario.register(prefix='control_fitosanitario', viewset=Control_fitosanitarioViewSet, basename='control_fitosanitario')