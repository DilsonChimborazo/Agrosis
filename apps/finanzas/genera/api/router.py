
from rest_framework.routers import DefaultRouter
from apps.finanzas.genera.api.views import GeneraViewSet
from apps.finanzas.genera.api.consumer import GeneraConsumer

from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack


router_Genera = DefaultRouter()
router_Genera.register(prefix="genera", basename="genera", viewset=GeneraViewSet)

websocket_urlpatterns = [
    re_path(r"ws/genera/$", GeneraConsumer.as_asgi()),  # Asegúrate de que coincida con la URL en WebSocket King
]