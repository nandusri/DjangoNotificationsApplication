from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from notifications.consumers import NotifierConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", NotifierConsumer),
    ])
})