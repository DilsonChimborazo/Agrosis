from rest_framework.routers import DefaultRouter
from apps.iot.sensores.api.views import SensoresViewSet
from django.urls import re_path
from apps.iot.sensores.api.consumer import SensoresConsumer

router_Sensores = DefaultRouter()
router_Sensores.register(prefix="sensores", basename="sensores", viewset=SensoresViewSet)

websocket_urlpatterns = [
    re_path(r'ws/sensores/$', SensoresConsumer.as_asgi()),
]