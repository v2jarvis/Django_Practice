"""
ASGI config for chatsystem project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import x_chatapp.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatsystem.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(x_chatapp.routing.websocket_urlpatterns)
        ),
    }
)
