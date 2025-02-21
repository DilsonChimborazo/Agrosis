from rest_framework.routers import DefaultRouter
from apps.usuarios.usuario.api.views import UsuarioViewsSet

routerUsuario = DefaultRouter()
routerUsuario.register(prefix='usuario', viewset=UsuarioViewsSet)


