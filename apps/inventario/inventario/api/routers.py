from rest_framework.routers import DefaultRouter
from .views import InsumoViewset, HerramientasViewset

router = DefaultRouter()
router.register(prefix='insumos', viewset=InsumoViewset)
router.register(prefix='herramientas', viewset=HerramientasViewset)