# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/whiteboard/(?P<room_name>\w+)/$", consumers.WhiteboardConsumer.as_asgi()),
    re_path(r"ws/whiteboard/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]