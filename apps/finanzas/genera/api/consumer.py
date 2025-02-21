import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models import Sum, F
from asgiref.sync import sync_to_async
from apps.finanzas.venta.models import Venta
from apps.finanzas.genera.models import Genera
from apps.finanzas.produccion.models import Produccion
from apps.trazabilidad.cultivo.models import Cultivo

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
        
        elif action == "producto_menos_vendido":
            result = await self.get_producto_menos_vendido()
            await self.send(text_data=json.dumps({"producto_menos_vendido": result}))
        
        elif action == "cultivo_mas_produce":
            result = await self.get_cultivo_mas_produce()
            await self.send(text_data=json.dumps({"cultivo_mas_produce": result}))
        
        elif action == "cultivo_menos_produce":
            result = await self.get_cultivo_menos_produce()
            await self.send(text_data=json.dumps({"cultivo_menos_produce": result}))

    @sync_to_async
    def get_producto_mas_vendido(self):
        producto = Venta.objects.values(
            'fk_id_produccion__genera__fk_id_cultivo__nombre_cultivo'
        ).annotate(
            total_vendido=Sum('cantidad'),
            total_precio=Sum(F('cantidad') * F('precio_unidad'))  # Corregido a precio_unidad
        ).order_by('-total_vendido').first()
        
        if producto:
            total_vendido = round(producto['total_vendido'], 2)
            total_precio = round(producto['total_precio'], 2)
            return f"{producto['fk_id_produccion__genera__fk_id_cultivo__nombre_cultivo']} con {total_vendido} unidades vendidas y un total de ${total_precio}"
        return "No hay datos de ventas"

    @sync_to_async
    def get_producto_menos_vendido(self):
        producto = Venta.objects.values(
            'fk_id_produccion__genera__fk_id_cultivo__nombre_cultivo'
        ).annotate(
            total_vendido=Sum('cantidad'),
            total_precio=Sum(F('cantidad') * F('precio_unidad'))  # Corregido a precio_unidad
        ).order_by('total_vendido').first()
        
        if producto:
            total_vendido = round(producto['total_vendido'], 2)
            total_precio = round(producto['total_precio'], 2)
            return f"{producto['fk_id_produccion__genera__fk_id_cultivo__nombre_cultivo']} con {total_vendido} unidades vendidas y un total de ${total_precio}"
        return "No hay datos de ventas"

    @sync_to_async
    def get_cultivo_mas_produce(self):
        cultivo = Genera.objects.values(
            'fk_id_cultivo__nombre_cultivo'
        ).annotate(
            total_produccion=Sum('fk_id_produccion__cantidad_produccion')
        ).order_by('-total_produccion').first()
        
        if cultivo:
            total_produccion = round(cultivo['total_produccion'], 2)
            return f"{cultivo['fk_id_cultivo__nombre_cultivo']} con {total_produccion} unidades producidas"
        return "No hay datos de producción"

    @sync_to_async
    def get_cultivo_menos_produce(self):
        cultivo = Genera.objects.values(
            'fk_id_cultivo__nombre_cultivo'
        ).annotate(
            total_produccion=Sum('fk_id_produccion__cantidad_produccion')
        ).order_by('total_produccion').first()
        
        if cultivo:
            total_produccion = round(cultivo['total_produccion'], 2)
            return f"{cultivo['fk_id_cultivo__nombre_cultivo']} con {total_produccion} unidades producidas"
        return "No hay datos de producción"
