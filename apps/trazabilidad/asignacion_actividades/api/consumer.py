import json
from channels.generic.websocket import AsyncWebsocketConsumer
from apps.trazabilidad.asignacion_actividades.models import Asignacion_actividades
from asgiref.sync import sync_to_async
from apps.usuarios.usuario.models import Usuarios
from apps.trazabilidad.actividad.models import Actividad
from channels.layers import get_channel_layer

class Asignacion_actividadesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Conexión WebSocket"""
        await self.channel_layer.group_add("asignacion_actividades", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Desconexión WebSocket"""
        await self.channel_layer.group_discard("asignacion_actividades", self.channel_name)

    async def receive(self, text_data):
        """Maneja los mensajes entrantes desde el cliente"""
        data = json.loads(text_data)

        # Verificar que los datos necesarios estén presentes
        if not all(key in data for key in ["fecha", "fk_id_actividad", "id_identificacion"]):
            await self.send(text_data=json.dumps({"error": "Faltan datos necesarios para asignar la actividad."}))
            return

        fecha = data["fecha"]
        fk_id_actividad = data["fk_id_actividad"]
        id_identificacion = data["id_identificacion"]

        # Lógica para asignar la actividad
        asignacion_actividades_data = await self.asignar_actividad(fecha, fk_id_actividad, id_identificacion)

        if asignacion_actividades_data:
            # Responder con los datos actuales de la asignación
            await self.send(text_data=json.dumps({"message": asignacion_actividades_data}))

            # Notificar a todos los usuarios conectados sobre la asignación de actividad
            await self.channel_layer.group_send(
                "asignacion_actividades",
                {
                    "type": "asignacion_actividades_data",
                    "message": asignacion_actividades_data
                }
            )
        else:
            await self.send(text_data=json.dumps({"error": "No se pudo asignar la actividad"}))

    async def asignacion_actividades_data(self, event):
        """Envía los datos de asignación de actividad al cliente en tiempo real"""
        await self.send(text_data=json.dumps({"message": event["message"]}))

    @sync_to_async
    def asignar_actividad(self, fecha, fk_id_actividad, id_identificacion):
        """Asigna la actividad en la base de datos y devuelve los datos"""
        try:
            # Obtener la instancia de la actividad a partir del ID
            actividad = Actividad.objects.get(id=fk_id_actividad)

            # Obtener la instancia del usuario a partir del ID
            usuario = Usuarios.objects.get(id=id_identificacion)

            # Asignar la actividad al usuario
            asignacion_actividades = Asignacion_actividades.objects.create(
                fecha=fecha,
                fk_id_actividad=actividad,  # Asigna la instancia de la actividad
                id_identificacion=usuario
            )

            # Obtener el nombre de la actividad desde fk_id_actividad
            actividad_nombre = asignacion_actividades.fk_id_actividad.nombre_actividad
            usuario_nombre = usuario.nombre
            usuario_apellido = usuario.apellido

            # Crear el mensaje para notificación
            return {
                "mensaje": f"{usuario_nombre} {usuario_apellido} Se le ha asignado la actividad {actividad_nombre} para realizarse el dia {asignacion_actividades.fecha}."
            }

        except Usuarios.DoesNotExist:
            return {"error": "El usuario no existe."}
        except Actividad.DoesNotExist:
            return {"error": "La actividad no existe."}
        except Exception as e:
            return {"error": str(e)}
