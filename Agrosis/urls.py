
from django.contrib import admin
from django.urls import path, include
from apps.usuarios.usuario.api.router import routerUsuario
from apps.usuarios.rol.api.router import routerRol
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
    path('api/', include(routerUsuario.urls)),
    path('api/', include(routerRol.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


    
