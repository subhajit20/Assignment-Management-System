# chat/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("join/<str:name>", consumers.ChatConsumer.as_asgi()),
]