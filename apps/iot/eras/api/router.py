from rest_framework.routers import DefaultRouter
from apps.iot.eras.api.views import ErasViewSet
from django.urls import re_path
from apps.iot.eras.api.consumer import ErasConsumer

router_Eras = DefaultRouter()
router_Eras.register(prefix="eras", basename="eras", viewset=ErasViewSet)


#ruta del websocked para eras
websocket_urlpatterns = [
    re_path(r'ws/eras/$', ErasConsumer.as_asgi()),
]