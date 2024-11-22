from rest_framework.routers import DefaultRouter
from apps.usuario.api.views import RolViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(prefix='rol', viewset=RolViewSet)
router.register(prefix='usuario', viewset=UsuarioViewSet) 