from rest_framework.routers import DefaultRouter
from apps.inventario.requiere.api.views import RequiereViewset

router_requiere =DefaultRouter()
router_requiere.register(prefix="requiere", basename= "requiere", viewset= RequiereViewset)