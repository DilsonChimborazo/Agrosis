import json
from channels.generic.websocket import AsyncWebsocketConsumer
from apps.iot.sensores.models import Sensores  
from asgiref.sync import sync_to_async

class SensoresConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Conexión WebSocket"""
        await self.channel_layer.group_add("sensores", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Desconexión WebSocket"""
        await self.channel_layer.group_discard("sensores", self.channel_name)

    async def receive(self, text_data):
        """Maneja los mensajes entrantes desde el cliente"""
        data = json.loads(text_data)

        if "nombre_sensor" in data:
            sensor_nombre = data["nombre_sensor"]

            # Obtener datos del sensor de la base de datos
            sensor_data = await self.get_sensor_data(sensor_nombre)

            if sensor_data:
                # Responder con los datos actuales del sensor
                await self.send(text_data=json.dumps({"message": sensor_data}))

                # También suscribimos al usuario a actualizaciones en tiempo real
                await self.channel_layer.group_send(
                    "sensores",
                    {
                        "type": "sensor_data",
                        "message": sensor_data
                    }
                )
            else:
                await self.send(text_data=json.dumps({"error": "Sensor no encontrado"}))

    async def sensor_data(self, event):
        """Envia los datos del sensor al cliente en tiempo real"""
        await self.send(text_data=json.dumps({"message": event["message"]}))

    @sync_to_async
    def get_sensor_data(self, nombre_sensor):
        """Consulta la base de datos para obtener la información del sensor"""
        try:
            sensor = Sensores.objects.get(nombre_sensor=nombre_sensor)
            return {
                "nombre_sensor": sensor.nombre_sensor,
                "medida_minima": sensor.medida_minima,
                "medida_maxima": sensor.medida_maxima,
                "dato enviado": sensor.medida_maxima / 3 
            }
        except Sensores.DoesNotExist:
            return None

