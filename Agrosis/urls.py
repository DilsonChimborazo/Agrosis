"""
URL configuration for Agrosis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.trazabilidad.actividad.api.router import router_actividad
from apps.trazabilidad.cultivo.api.router import router_cultivo
from apps.trazabilidad.residuos.api.router import router_residuos
from apps.trazabilidad.tipo_residuos.api.router import router_tipo_residuos
from apps.trazabilidad.control_fitosanitario.api.router import router_control_fitosanitario
from apps.trazabilidad.desarrollan.api.router import router_desarrollan
from apps.trazabilidad.plantacion.api.router import router_plantacion
from apps.trazabilidad.pea.api.router import router_pea

from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="documentacion API",
      default_version='v0.1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

urlpatterns = [
   path('admin/', admin.site.urls),
   
   path('api/', include(router_actividad.urls)),
   path('api/', include(router_cultivo.urls)),
   path('api/', include(router_tipo_residuos.urls)),
   path('api/', include(router_control_fitosanitario.urls)),
   path('api/', include(router_desarrollan.urls)),
   path('api/', include(router_plantacion.urls)),
   path('api/', include(router_pea.urls)),
   path('api/', include(router_residuos.urls)),
   
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]
