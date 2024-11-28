from rest_framework.routers import DefaultRouter
from apps.inventario.control_usa_insumo.api.views import ControlUsaInsumoViewset

router_usa =DefaultRouter()
router_usa.register(prefix="usa", basename= "usa", viewset= ControlUsaInsumoViewset)