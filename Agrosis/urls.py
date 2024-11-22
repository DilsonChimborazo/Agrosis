
from django.contrib import admin
from django.urls import path, include
from apps.trazabilidad.api.router import router_actividad, router_asignacion_actividad, router_control_uso_insumo, router_especie, router_notificacion, router_programacion, router_realiza, router_semillero, router_tipo_cultivo, router_calendario_lunar, router_ubicacion, router_lote, router_eras, router_cultivo, router_plantacion, router_pea, router_desarrollan, router_tipo_residuos, router_residuos, router_control_fitosanitario

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
]
