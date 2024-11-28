from rest_framework.routers import DefaultRouter
from apps.usuarios.rol.api.views import RolViewSet

router = DefaultRouter()
router.register(prefix='rol', viewset=RolViewSet)