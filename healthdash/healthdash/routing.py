from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from dashboard import consumer

websocket_urlPattern=[
    path(r'ws/polData/',consumer.DashConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))
})