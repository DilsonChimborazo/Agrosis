import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from apps.iot.eras.models import Eras  

class ErasConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Conexión WebSocket"""
        await self.channel_layer.group_add("eras", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Desconexión WebSocket"""
        await self.channel_layer.group_discard("eras", self.channel_name)

    async def receive(self, text_data):
        """Maneja los mensajes entrantes desde el cliente"""
        data = json.loads(text_data)

        if "fk_id_lote" in data:
            fk_id_lote = data["fk_id_lote"]

            # Obtener datos de las eras asociadas al lote
            eras_data = await self.get_eras_data(fk_id_lote)

            if eras_data:
                # Responder con los datos actuales de las eras
                await self.send(text_data=json.dumps({"message": eras_data}))

                # Enviar actualización en tiempo real al grupo "eras"
                await self.channel_layer.group_send(
                    "eras",
                    {
                        "type": "eras_data",
                        "message": eras_data
                    }
                )
            else:
                await self.send(text_data=json.dumps({"error": "No se encontraron eras para este lote"}))

    async def eras_data(self, event):
        """Envía los datos de las eras al cliente en tiempo real"""
        await self.send(text_data=json.dumps({"message": event["message"]}))

    @sync_to_async
    def get_eras_data(self, fk_id_lote):
        """Consulta la base de datos para obtener las eras asociadas a un lote"""
        eras = Eras.objects.filter(fk_id_lote=fk_id_lote).values("id", "descripcion")
        return list(eras) if eras.exists() else None
