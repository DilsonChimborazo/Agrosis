import json
from channels.generic.websocket import AsyncWebsocketConsumer
from apps.trazabilidad.asignacion_actividades.models import Asignacion_actividades  
from asgiref.sync import sync_to_async

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

        if "nombre_asignacion_actividades" in data:
            asignacion_actividades_nombre = data["nombre_asignacion_actividades"]

            # Obtener datos del asignacion_actividades de la base de datos
            asignacion_actividades_data = await self.get_asignacion_actividades_data(asignacion_actividades_nombre)

            if asignacion_actividades_data:
                # Responder con los datos actuales del asignacion_actividades
                await self.send(text_data=json.dumps({"message": asignacion_actividades_data}))

                # También suscribimos al usuario a actualizaciones en tiempo real
                await self.channel_layer.group_send(
                    "asignacion_actividades",
                    {
                        "type": "asignacion_actividades_data",
                        "message": asignacion_actividades_data
                    }
                )
            else:
                await self.send(text_data=json.dumps({"error": "asignacion_actividades no encontrado"}))

    async def asignacion_actividades_data(self, event):
        """Envia los datos del asignacion_actividades al cliente en tiempo real"""
        await self.send(text_data=json.dumps({"message": event["message"]}))

    @sync_to_async
    def get_asignacion_actividades_data(self, fecha, fk_id_actividad, id_identificacion):
        """Consulta la base de datos para obtener la información de asignacion_actividades"""
        try:
            asignacion_actividades = asignacion_actividades.objects.get(fecha=fecha, fk_id_actividad=fk_id_actividad, id_identificacion=id_identificacion)
            return {
                "fecha": asignacion_actividades.fecha,
                "fk_id_actividad": asignacion_actividades.fk_id_actividad,
                "id_identificacion": asignacion_actividades.id_identificacion,
                 
            }
        except asignacion_actividades.DoesNotExist:
            return None
