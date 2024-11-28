from rest_framework.routers import DefaultRouter
from apps.usuarios.usuario.api.views import UsuarioViewsSet

router = DefaultRouter()
router.register(prefix='usuario', viewset=UsuarioViewsSet) 