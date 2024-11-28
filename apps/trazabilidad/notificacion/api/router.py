from rest_framework.routers import DefaultRouter
from apps.trazabilidad.notificacion.api.views import NotificacionModelViewSet

# Crear routers específicos para el ViewSet de Notificacion
routerNotificacion = DefaultRouter()
routerNotificacion.register(prefix='notificaciones', viewset=NotificacionModelViewSet, basename='notificaciones')

# Exportar los routers como un diccionario
routers = {
    'notificaciones': routerNotificacion,
}
