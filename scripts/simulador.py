import os
import django
import random
import asyncio
import json
import websockets
from django.utils.timezone import now
from asgiref.sync import sync_to_async

# Configurar Django para acceder a los modelos
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Agrosis.settings")
django.setup()

from apps.iot.sensores.models import Sensores
from apps.iot.mide.models import Mide

@sync_to_async
def obtener_sensores():
    """ Obtiene todos los sensores registrados en la base de datos """
    return list(Sensores.objects.all())

@sync_to_async
def guardar_medicion(sensor, valor):
    """ Guarda el valor medido en la tabla Mide """
    return Mide.objects.create(
        fk_id_sensor=sensor,
        fk_id_era=None,  # Ajusta según la lógica de tu aplicación
        valor_medicion=valor,
        fecha_medicion=now()
    )

async def send_random_data():
    """ Simula el envío de datos de sensores a WebSockets """
    uri = "ws://localhost:8000/ws/sensores/"
    async with websockets.connect(uri) as websocket:
        while True:
            sensores = await obtener_sensores()

            if sensores:
                sensor = random.choice(sensores)
                valor = round(random.uniform(sensor.medida_minima - 10, sensor.medida_maxima + 10), 2)

                data = {
                    "sensor_id": sensor.id,
                    "valor": valor,
                }

                # Enviar datos al WebSocket
                await websocket.send(json.dumps(data))
                print(f"📡 Enviando datos: {data}")

                # Guardar la medición en la base de datos
                await guardar_medicion(sensor, valor)

            await asyncio.sleep(10)  # Enviar datos cada 5 segundos

def run():
    """ Ejecuta el simulador correctamente con Django """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_random_data())
