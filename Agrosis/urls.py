
from django.contrib import admin
from django.urls import path, include
from apps.trazabilidad.api.router import *

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.inventario.api.routers import router_inventario
from apps.finanzas.api.router import router_ventas
from apps.iot.api.router import router_iot
from apps.usuario.api.router import router_usuario

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('api/finanzas', include(router_ventas.urls)),
   path('api/inventario', include(router_inventario.urls)),
   path('api/iot', include(router_iot.urls)),
   path('api/trazabilidad', include(router_trazabilidad.urls)),
   path('api/usuario/', include(router_usuario.urls)),
]
