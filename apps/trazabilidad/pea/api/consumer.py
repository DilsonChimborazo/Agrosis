import json
from channels.generic.websocket import AsyncWebsocketConsumer
from apps.trazabilidad.pea.models import Pea
from asgiref.sync import sync_to_async

class PeaConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Conexión WebSocket"""
        await self.channel_layer.group_add("pea", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Desconexión WebSocket"""
        await self.channel_layer.group_discard("pea", self.channel_name)

    async def receive(self, text_data):
        """Maneja los mensajes entrantes desde el cliente"""
        data = json.loads(text_data)
        
        if "nombre_pea" in data:
            pea_nombre = data["nombre_pea"]

            
            pea_data = await self.get_pea_data(pea_nombre)

            if pea_data:
               
                await self.send(text_data=json.dumps({"message": pea_data}))

               
                await self.channel_layer.group_send(
                    "pea",
                    {
                        "type": "pea_data",
                        "message": pea_data
                    }
                )
            else:
                await self.send(text_data=json.dumps({"error": "pea no encontrada"}))

    async def pea_data(self, event):
        """Envia los datos del pea al cliente en tiempo real"""
        await self.send(text_data=json.dumps({"message": event["message"]}))

    @sync_to_async
    def get_pea_data(self, nombre_pea):
        """Consulta la base de datos para obtener la información del pea"""
        try:
            pea = Pea.objects.get(nombre_pea=nombre_pea)
            return {
                "nombre_pea": pea.nombre_pea,
                "descripcion": pea.descripcion,
                
                "dato enviado": pea.nombre_pea / 3 
            }
        except Pea.DoesNotExist:
            return None
