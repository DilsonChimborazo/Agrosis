from rest_framework.routers import DefaultRouter
from apps.inventario.api.views import *

router_inventario = DefaultRouter()
router_inventario.register(prefix='insumos', viewset=InsumoViewset)
router_inventario.register(prefix='herramientas', viewset=HerramientasViewset)
router_inventario.register(prefix='requiere', viewset=RequiereViewset)
router_inventario.register(prefix='utiliza', viewset=UtilizaViewset)
router_inventario.register(prefix='control_uso_insumos', viewset=ControlUsoInsumoModelViewSet, basename='control_uso_insumos')