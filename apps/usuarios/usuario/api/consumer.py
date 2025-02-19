import json
from channels.generic.websocket import AsyncWebsocketConsumer
from apps.usuarios.usuario.models import Usuarios
from asgiref.sync import sync_to_async
from datetime import date, datetime

class UsuariosConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Conexión WebSocket"""
        await self.channel_layer.group_add("usuarios", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Desconexión WebSocket"""
        await self.channel_layer.group_discard("usuarios", self.channel_name)

    async def receive(self, text_data):
        """Maneja los mensajes entrantes desde el cliente"""
        data = json.loads(text_data)

        if "fk_id_rol" in data:
            fk_id_rol = data["fk_id_rol"]

            # Obtener datos del sensor de la base de datos
            usuarios_data = await self.get_usuarios(fk_id_rol)

            if usuarios_data:
                # Responder con los datos actuales del sensor
                await self.send(text_data=json.dumps({"message": usuarios_data}))

                # También suscribimos al usuario a actualizaciones en tiempo real
                await self.channel_layer.group_send(
                    "usuarios",
                    {
                        "type": "usuarios",
                        "message": usuarios_data
                    }
                )
            else:
                await self.send(text_data=json.dumps({"error": "Usuario no encontrado"}))

    async def usuarios(self, event):
        """Envia los datos del sensor al cliente en tiempo real"""
        await self.send(text_data=json.dumps({"message": event["message"]}))

    @sync_to_async
    def get_usuarios(self, fk_id_rol):
        """Consulta la base de datos para obtener la información del sensor"""
        try:
            usuario = Usuarios.objects.get(fk_id_rol = fk_id_rol)
            rol = usuario.fk_id_rol

            def format_date(fecha):
                if isinstance(fecha, (date, datetime)):
                    return fecha.strftime("%Y-%m-%d %H:%M:%S")
                return fecha  

            rol_data = {
                "rol": rol.rol,
                "actualizacion": format_date (rol.actualizacion),
                "fecha_creacion": format_date (rol.fecha_creacion)
            }if rol else None
            return {
                "fk_id_rol": rol_data,
                "nombre": usuario.nombre,
                "apellido": usuario.apellido,
                "email": usuario.email
            }
        except Usuarios.DoesNotExist:
            return None

