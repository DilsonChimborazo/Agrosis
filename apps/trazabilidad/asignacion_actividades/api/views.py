from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from apps.trazabilidad.asignacion_actividades.models import Asignacion_actividades
from apps.trazabilidad.asignacion_actividades.api.serializers import (LeerAsignacion_actividadesSerializer,EscribirAsignacion_actividadesSerializer)
from apps.usuarios.usuario.models import Usuarios
from apps.trazabilidad.actividad.models import Actividad


class Asignacion_actividadesModelViewSet(ModelViewSet):
    permissions_clases = [IsAuthenticatedOrReadOnly]
    queryset = Asignacion_actividades.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LeerAsignacion_actividadesSerializer
        return EscribirAsignacion_actividadesSerializer

    def create(self, request, *args, **kwargs):
        """ Sobreescribe el método POST para incluir el mensaje personalizado y enviar notificación por WebSocket """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            asignacion = serializer.save()

            # Obtener información del usuario y actividad
            usuario = Usuarios.objects.get(id=asignacion.id_identificacion.id)
            actividad = Actividad.objects.get(id=asignacion.fk_id_actividad.id)

            mensaje = {
                "mensaje": f"{usuario.nombre} {usuario.apellido} Se le ha asignado la actividad {actividad.nombre_actividad} para realizarse el dia {asignacion.fecha}."
            }

            # 🔥 Notificación en tiempo real con WebSockets
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "asignacion_actividades",  # Grupo WebSocket
                {
                    "type": "asignacion_actividades_data",
                    "message": mensaje
                }
            )

            return Response(mensaje, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
