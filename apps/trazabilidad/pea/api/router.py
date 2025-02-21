from rest_framework.routers import DefaultRouter
from apps.trazabilidad.pea.api.views import PeaViewSet
from django.urls import re_path
from apps.trazabilidad.pea.api.consumer import PeaConsumer


router_pea = DefaultRouter()
router_pea.register(prefix='pea', viewset=PeaViewSet, basename='pea')

websocket_urlpatterns = [
    re_path(r'ws/pea/$', PeaConsumer.as_asgi()),
]