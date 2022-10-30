from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from json import dumps
from channels.layers import get_channel_layer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.name = self.scope["url_route"]["kwargs"]["name"]
        self.accept()
        data = {
            "msg":"Hellow! Wellcome",
            "id":self.channel_name,
            "name":self.name
        }
        self.send(text_data=dumps(data))
        
    def receive(self, text_data=None, bytes_data=None):
        self.send(text_data=text_data)

    def disconnect(self):
        
        self.close()