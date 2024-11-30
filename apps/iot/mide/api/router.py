from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.iot.mide.api.views import MideViewSet



router_mide = DefaultRouter()
router_mide.register(prefix="mide", viewset=MideViewSet)

urlpatterns = [
    path('api/', include(router_mide.urls)),
]