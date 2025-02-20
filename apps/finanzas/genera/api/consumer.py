import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models import Sum
from apps.finanzas.venta.models import Venta
from apps.finanzas.genera.models import Genera
from apps.finanzas.produccion.models import Produccion

class GeneraConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Conexión establecida"}))

    async def disconnect(self, close_code):
        print(f"WebSocket cerrado con código: {close_code}")

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")

        if action == "producto_mas_vendido":
            result = await self.get_producto_mas_vendido()
            await self.send(text_data=json.dumps({"producto_mas_vendido": result}))

        elif action == "cultivo_mas_generado":
            result = await self.get_cultivo_mas_generado()
            await self.send(text_data=json.dumps({"cultivo_mas_generado": result}))

    async def get_producto_mas_vendido(self):
        producto = Venta.objects.values('fk_id_produccion__id_produccion') \
            .annotate(total_vendido=Sum('cantidad')) \
            .order_by('-total_vendido') \
            .first()
        
        if producto:
            return f"Producción ID {producto['fk_id_produccion__id_produccion']} con {producto['total_vendido']} unidades vendidas"
        return "No hay datos de ventas"

    async def get_cultivo_mas_generado(self):
        cultivo = Genera.objects.values('fk_id_cultivo__nombre') \
            .annotate(total_generado=Sum('fk_id_produccion__cantidad_produccion')) \
            .order_by('-total_generado') \
            .first()

        if cultivo:
            return f"Cultivo {cultivo['fk_id_cultivo__nombre']} con {cultivo['total_generado']} unidades producidas"
        return "No hay datos de producción"
