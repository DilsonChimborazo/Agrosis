from rest_framework.routers import DefaultRouter
from apps.inventario.utiliza.api.views import UtilizaViewset


router_utiliza =DefaultRouter()
router_utiliza.register(prefix="utiliza", basename= "utiliza", viewset= UtilizaViewset)

