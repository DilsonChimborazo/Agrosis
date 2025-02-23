import json
from channels.generic.websocket import AsyncWebsocketConsumer
from apps.iot.sensores.models import Sensores
from apps.iot.mide.models import Mide
from django.utils.timezone import now

class SensorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.group_name = "sensor_alerts"
        await self.channel_layer.group_add(self.group_name, self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        sensor_id = data.get("sensor_id")
        valor_medicion = float(data.get("valor"))

        sensor = await self.get_sensor(sensor_id)

        if sensor:
            if valor_medicion < sensor.medida_minima or valor_medicion > sensor.medida_maxima:
                await self.send_alert(sensor, valor_medicion)

            await self.save_measurement(sensor, valor_medicion)

    async def send_alert(self, sensor, valor):
        message = {
            "alerta": f"¡ALERTA! El sensor {sensor.nombre_sensor} {sensor.tipo_sensor} ha salido de su rango permitido.",
            "valor": valor
        }
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "send_notification",
                "message": message,
            },
        )

    async def send_notification(self, event):
        await self.send(text_data=json.dumps(event["message"]))

    @staticmethod
    async def get_sensor(sensor_id):
        return await Sensores.objects.filter(id=sensor_id).afirst()

    @staticmethod
    async def save_measurement(sensor, valor):
        await Mide.objects.acreate(
            fk_id_sensor=sensor,
            fk_id_era=None,  # Puedes modificar esto según tu lógica
            valor_medicion=valor,
            fecha_medicion=now()
        )