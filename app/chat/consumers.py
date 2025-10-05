import json
from channels.consumer import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Group, Message


class PrivateMessageConsumer(WebsocketConsumer):
    def connect(self):
        print("something is going on")
        self.room_name = self.scope["url_route"]["kwargs"]["uuid"]
        self.room_group_name = f"chat_{self.room_name}"
        self.group = Group.objects.get(uuid=self.room_name)
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
        self.group.messages.create(text=message, user=self.scope["user"])
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message,
                "user_uuid": str(self.scope["user"].uuid),
                "username": self.scope["user"].username,
            },
        )

    # Receive message from room group
    def chat_message(self, event):
        self.send(
            text_data=json.dumps(
                {
                    "message": event["message"],
                    "user_uuid": event["user_uuid"],
                    "username": event["username"],
                }
            )
        )

