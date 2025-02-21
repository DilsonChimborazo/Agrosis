"""
ASGI config for Agrosis project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Agrosis.settings')  # Asegurar la configuración
django.setup()  # 🔹 Inicializar Django antes de importar cualquier módulo relacionado con él


from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from .routing import websocket_urlpatterns



application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(  # Agregamos AuthMiddlewareStack para WebSockets autenticados
        URLRouter(websocket_urlpatterns)
    ),
})