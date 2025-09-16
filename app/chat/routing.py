from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r"chat/<uuid:uuid>/)/$", consumers.PrivateMessageConsumer.as_asgi()),
]