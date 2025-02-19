from rest_framework.routers import DefaultRouter
from apps.usuarios.usuario.api.views import UsuarioViewsSet
from django.urls import re_path
from apps.usuarios.usuario.api.consumer import UsuariosConsumer

routerUsuario = DefaultRouter()
routerUsuario.register(prefix='usuario', viewset=UsuarioViewsSet)

websocket_urlpatterns = [
    re_path(r'ws/usuarios/$', UsuariosConsumer.as_asgi()),
]
