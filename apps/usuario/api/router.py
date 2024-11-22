from rest_framework.routers import DefaultRouter
from apps.usuario.api.views import RolViewSet, UsuarioViewSet

router_usuario = DefaultRouter()
router_usuario.register(prefix='rol', viewset=RolViewSet)
router_usuario.register(prefix='usuario', viewset=UsuarioViewSet) 