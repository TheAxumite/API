from django.http import HttpResponse
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .views import socket_view

# Websocket consumer to handle the socket connection
# In your Django Channels routing configuration, you would route the websocket connection to this consumer


class SocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        # Process the received data here
        print(text_data)

    async def disconnect(self, close_code):
        pass

    def send_to_view(self, event):
        # Send the received data to the socket_view
        request = type('Request', (object,), {'body': event['data'].encode('utf-8')})
        response = socket_view(request)

        # Send the response back to the consumer
        self.send(text_data=response.content.decode('utf-8'))