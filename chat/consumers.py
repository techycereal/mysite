import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

# Store the whiteboard state in memory for simplicity.
# You might want to use a more persistent storage for a production app.
whiteboard_state = {}

class WhiteboardConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'whiteboard_{self.room_name}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        if self.room_group_name not in whiteboard_state:
            whiteboard_state[self.room_group_name] = []
        # Send the current state of the whiteboard to the new user
        self.send(text_data=json.dumps({
            'type': 'current_state',
            'state': whiteboard_state[self.room_group_name]
        }))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        drawing_data = data['drawing_data']
        # Add the new drawing data to the whiteboard state
        whiteboard_state[self.room_group_name].append(drawing_data)

        # Send drawing data to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'whiteboard_drawing',
                'drawing_data': drawing_data
            }
        )

    def whiteboard_drawing(self, event):
        drawing_data = event['drawing_data']

        # Send drawing data to WebSocket
        self.send(text_data=json.dumps({
            'drawing_data': drawing_data
        }))


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message, "username": username}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        print(username)
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, "username": username}))