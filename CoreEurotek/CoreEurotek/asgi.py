"""
ASGI config for CoreEurotek project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from report.notifications.middlewares import WebSocketNotificationMiddleware
from report import routers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CoreEurotek.settings')

django_asgi_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_application,
        "websocket": WebSocketNotificationMiddleware(URLRouter(routers.websocket_patterns))
    }
)
