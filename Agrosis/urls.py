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
from apps.trazabilidad.asignacion_actividades.api.router import routerAsignacion_actividades
from apps.trazabilidad.calendario_lunar.api.router import routerCalendario_lunar
from apps.trazabilidad.especie.api.router import routerEspecie
from apps.trazabilidad.notificacion.api.router import routerNotificacion
from apps.trazabilidad.programacion.api.router import routerProgramacion
from apps.trazabilidad.realiza.api.router import routerRealiza
from apps.trazabilidad.semillero.api.router import routerSemillero
from apps.trazabilidad.tipo_cultivo.api.router import routerTipo_cultivo

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
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),


    path('api/', include(routerAsignacion_actividades.urls)),
    path('api/', include(routerCalendario_lunar.urls)),
    path('api/', include(routerEspecie.urls)),
    path('api/', include(routerRealiza.urls)),
    path('api/', include(routerTipo_cultivo.urls)),
    path('api/', include(routerSemillero.urls)),
    path('api/', include(routerProgramacion.urls)),
    path('api/', include(routerNotificacion.urls)),
   
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
