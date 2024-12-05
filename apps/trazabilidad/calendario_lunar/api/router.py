from rest_framework.routers import DefaultRouter
from apps.trazabilidad.calendario_lunar.api.views import Calendario_lunarModelViewSet

# Crear routers específicos para el ViewSet de CalendarioLunar
routerCalendario_lunar = DefaultRouter()
routerCalendario_lunar.register(prefix='calendario_lunar', viewset=Calendario_lunarModelViewSet, basename='calendario_lunar')

# Exportar los routers como un diccionario
routers = {
    'calendario_lunar': routerCalendario_lunar,
}
